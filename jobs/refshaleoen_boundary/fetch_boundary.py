import osmnx as ox
import geopandas as gpd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_RAW_DIR = ROOT_DIR / "data" / "raw"
DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = DATA_RAW_DIR / "refshaleoen_boundary.geojson"

def fetch_refshaleoen():
    print("Fetching Refshaleøen boundary from OpenStreetMap...")
    
    queries = [
        "Refshaleøen, Copenhagen, Denmark",
        "Refshaleøen, Denmark"
    ]
    
    for query in queries:
        try:
            print(f"Trying query: '{query}'")
            gdf = ox.geocode_to_gdf(query)
            gdf.to_file(OUTPUT_FILE, driver="GeoJSON")
            print(f"Successfully saved boundary to {OUTPUT_FILE}")
            return
        except Exception as e:
            print(f"Failed for '{query}': {e}")
            
    print("Could not fetch the boundary using OSMnx.")

if __name__ == "__main__":
    fetch_refshaleoen()
