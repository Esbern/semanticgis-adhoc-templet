import os
import requests

url = "https://graphql.datafordeler.dk/GEODKV/v1"
api_key = os.getenv("DATAFORDELER_API_KEY")
if not api_key:
    raise SystemExit("Missing DATAFORDELER_API_KEY in environment")

params = {"apikey": api_key}

roots = [
    "vejmidte", "geodanmarkVejmidte", "geodk_vejmidte", "hentVejmidte", "soegVejmidte", 
    "geodanmark_vejmidte", "Vejmidte", "vejkant"
]

for root in roots:
    query = f"query {{ {root}(first: 1) {{ id }} }}"
    r = requests.post(url, params=params, json={"query": query})
    if "does not exist on the type" not in r.text:
        print(f"Match found for root: {root}")
        print(r.text[:200])
