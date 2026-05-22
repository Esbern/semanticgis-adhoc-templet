import os
import requests
import geopandas as gpd
import osmnx as ox
import pandas as pd
from shapely import wkt
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATAFORDELER_API_KEY = os.getenv("DATAFORDELER_API_KEY")
GRAPHQL_URL = "https://graphql.datafordeler.dk/GEODKV/v1"

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_RAW_DIR = ROOT_DIR / "data" / "raw"
DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)

def fetch_layer_graphql(layer_name, token, boundary_wkt):
    print(f"Fetching layer via GraphQL: {layer_name}...")
    
    query_template = """
    query($wkt: String!, $after: String) {
      %s(
        first: 1000
        after: $after
        virkningstid: "2026-04-25T13:00:00Z"
        where: {
          geometri: {
            intersects: { wkt: $wkt, crs: 25832 }
          }
        }
      ) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id_lokalId
          geometri { wkt }
        }
      }
    }
    """ % layer_name

    variables = {
        "wkt": boundary_wkt,
        "after": None
    }
    
    params = {"apikey": token}
    
    all_features = []
    has_next = True
    
    while has_next:
        response = requests.post(
            GRAPHQL_URL, 
            params=params, 
            json={"query": query_template, "variables": variables}
        )
        if response.status_code != 200:
            print(f"Failed to fetch {layer_name}. Status: {response.status_code}")
            print(response.text[:200])
            break
            
        data = response.json()
        if "errors" in data:
            print(f"GraphQL Errors for {layer_name}: {data['errors']}")
            break
            
        layer_data = data.get("data", {}).get(layer_name, {})
        nodes = layer_data.get("nodes", [])
        
        for node in nodes:
            geom_dict = node.get("geometri")
            if geom_dict and geom_dict.get("wkt"):
                try:
                    geometry = wkt.loads(geom_dict["wkt"])
                    all_features.append({
                        "id_lokalId": node.get("id_lokalId"),
                        "geometry": geometry
                    })
                except Exception as e:
                    pass
        
        page_info = layer_data.get("pageInfo", {})
        has_next = page_info.get("hasNextPage", False)
        if has_next:
            variables["after"] = page_info.get("endCursor")
            print(f"  Fetched {len(all_features)} items, fetching next page...")

    if not all_features:
        return gpd.GeoDataFrame()
        
    gdf = gpd.GeoDataFrame(all_features, geometry="geometry", crs="EPSG:25832")
    return gdf

def main():
    if not DATAFORDELER_API_KEY:
        print("Error: DATAFORDELER_API_KEY not found in .env")
        return

    print("Fetching Rødovre Municipality boundary using OSMnx...")
    try:
        roedovre_gdf = ox.geocode_to_gdf("Rødovre Municipality, Denmark")
    except Exception as e:
        print(f"Failed to fetch boundary: {e}")
        return
        
    # Project to EPSG:25832 for Datafordeleren WKT intersection
    roedovre_gdf_25832 = roedovre_gdf.to_crs("EPSG:25832")
    boundary_geom_25832 = roedovre_gdf_25832.geometry.iloc[0]
    # WKT representation - use envelope to prevent Max GraphQL request size reached error
    boundary_wkt = boundary_geom_25832.envelope.wkt
    
    # Keeping EPSG:4326 for clipping after fetching
    boundary_geom_4326 = roedovre_gdf.geometry.iloc[0]
    
    layers = {
        "roads": ["GEODKV_Vejmidte"],
        "buildings": ["GEODKV_Bygning"],
        "green_areas": ["GEODKV_Skov", "GEODKV_KratBevoksning", "GEODKV_Vaadomraade"]
    }
    
    for category, layer_list in layers.items():
        gdfs = []
        for layer in layer_list:
            gdf = fetch_layer_graphql(layer, DATAFORDELER_API_KEY, boundary_wkt)
            if not gdf.empty:
                print(f"Projecting {layer} to EPSG:4326 and clipping to exact boundary...")
                gdf_4326 = gdf.to_crs("EPSG:4326")
                gdf_clipped = gpd.clip(gdf_4326, boundary_geom_4326)
                if not gdf_clipped.empty:
                    # Add layer name for distinction
                    gdf_clipped['layer'] = layer
                    gdfs.append(gdf_clipped)
        
        if gdfs:
            combined = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))
            out_file = DATA_RAW_DIR / f"roedovre_{category}.geojson"
            combined.to_file(out_file, driver="GeoJSON")
            print(f"Saved {category} to {out_file} ({len(combined)} features)")
        else:
            print(f"No data found for {category}")

if __name__ == "__main__":
    main()
