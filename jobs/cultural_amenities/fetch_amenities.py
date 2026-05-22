import geopandas as gpd
import osmnx as ox
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
INPUT_FILE = ROOT_DIR / "data" / "edits" / "raffen.gpkg"
OUTPUT_FILE = ROOT_DIR / "data" / "raw" / "cultural_amenities.geojson"

def main():
    print(f"Reading boundary from {INPUT_FILE}...")
    try:
        gdf_boundary = gpd.read_file(INPUT_FILE)
    except Exception as e:
        print(f"Failed to read input file: {e}")
        return
        
    # Project to EPSG:4326 if needed, as OSMnx expects lat/lon
    if gdf_boundary.crs != "EPSG:4326":
        gdf_boundary = gdf_boundary.to_crs("EPSG:4326")
    
    # Fix potentially invalid geometries resulting from manual QGIS edits
    gdf_boundary.geometry = gdf_boundary.geometry.buffer(0)
    
    boundary_poly = gdf_boundary.unary_union
    
    # If unary_union creates a MultiPolygon or leaves it invalid, ensure it's valid
    if not boundary_poly.is_valid:
        boundary_poly = boundary_poly.buffer(0)
    
    tags = {
        'amenity': ['arts_centre', 'theatre', 'cinema', 'community_centre', 'library', 'events_venue'],
        'tourism': ['museum', 'gallery', 'artwork']
    }
    
    print("Fetching cultural amenities from OpenStreetMap within the boundary...")
    try:
        pois = ox.features_from_polygon(boundary_poly, tags)
        
        if pois.empty:
            print("No cultural amenities found.")
            pois.to_file(OUTPUT_FILE, driver="GeoJSON")
        else:
            # Clean columns that might contain lists/dicts
            for col in pois.columns:
                pois[col] = pois[col].apply(lambda x: str(x) if isinstance(x, (list, dict)) else x)
                
            pois.to_file(OUTPUT_FILE, driver="GeoJSON")
            print(f"Successfully found {len(pois)} amenities and saved to {OUTPUT_FILE}")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
