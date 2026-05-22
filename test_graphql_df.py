import requests

url = "https://api.dataforsyningen.dk/graphql"
params = {
    "token": "h9b5nJDYLX92VF2YC3Jf7IM2a6U5f5nXXgkFXhQkXNSZtYJ1xLomdiS0gFo9VF5TUBmPQi5UfCHqeO7OmPh79batxhXda3zgM"
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
