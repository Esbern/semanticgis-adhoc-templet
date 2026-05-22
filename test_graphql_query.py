import requests

url = "https://graphql.datafordeler.dk/GEODKV/v1"
params = {
    "apikey": "h9b5nJDYLX92VF2YC3Jf7IM2a6U5f5nXXgkFXhQkXNSZtYJ1xLomdiS0gFo9VF5TUBmPQi5UfCHqeO7OmPh79batxhXda3zgM"
}

query = """
query {
  bygning(first: 1) {
    id
    geometri
  }
}
"""

try:
    r = requests.post(url, params=params, json={"query": query})
    print("Status:", r.status_code)
    print("Response:", r.text[:500])
except Exception as e:
    print(e)
