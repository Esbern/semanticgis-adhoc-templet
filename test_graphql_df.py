import os
import requests

url = "https://api.dataforsyningen.dk/graphql"
token = os.getenv("DATAFORSYNINGEN_TOKEN")
if not token:
  raise SystemExit("Missing DATAFORSYNINGEN_TOKEN in environment")

params = {
  "token": token,
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
