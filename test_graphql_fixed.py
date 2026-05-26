import os
import requests
import json

url = "https://graphql.datafordeler.dk/GEODKV/v1"
api_key = os.getenv("DATAFORDELER_API_KEY")
if not api_key:
  raise SystemExit("Missing DATAFORDELER_API_KEY in environment")

params = {
  "apikey": api_key,
}

query = """
query {
  __schema {
    types {
      name
    }
  }
}
"""

try:
    r = requests.post(url, params=params, json={"query": query})
    print("Status:", r.status_code)
    print("Response:", r.text[:300])
except Exception as e:
    print(e)
