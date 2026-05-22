import requests

url = "https://graphql.datafordeler.dk/GEODKV/v1/schema"
params = {"apikey": "h9b5nJDYLX92VF2YC3Jf7IM2a6U5f5nXXgkFXhQkXNSZtYJ1xLomdiS0gFo9VF5TUBmPQi5UfCHqeO7OmPh79batxhXda3zgM"}

try:
    r = requests.get(url, params=params)
    print("Status:", r.status_code)
    if r.status_code == 200:
        with open("schema_geodkv.graphql", "w") as f:
            f.write(r.text)
        print("Schema saved to schema_geodkv.graphql")
    else:
        print(r.text[:500])
except Exception as e:
    print(e)
