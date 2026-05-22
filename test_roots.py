import requests

url = "https://graphql.datafordeler.dk/GEODKV/v1"
params = {"apikey": "h9b5nJDYLX92VF2YC3Jf7IM2a6U5f5nXXgkFXhQkXNSZtYJ1xLomdiS0gFo9VF5TUBmPQi5UfCHqeO7OmPh79batxhXda3zgM"}

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
