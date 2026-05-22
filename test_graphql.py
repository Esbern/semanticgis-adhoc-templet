import requests
import json

url = "https://graphql.datafordeler.dk/GEODKV/v1"
params = {
    "apikey": "81512860b82d0f1a8814a5775e088ba4"
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
