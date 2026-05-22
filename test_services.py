import requests
import json
url = "https://api.dataforsyningen.dk/rest/services"
token = "h9b5nJDYLX92VF2YC3Jf7IM2a6U5f5nXXgkFXhQkXNSZtYJ1xLomdiS0gFo9VF5TUBmPQi5UfCHqeO7OmPh79batxhXda3zgM"
try:
    r = requests.get(url, params={"token": token})
    if r.status_code == 200:
        data = r.json()
        print("Total services:", len(data))
        for srv in data:
            if "geodanmark" in srv.get("name", "").lower() or "fot" in srv.get("name", "").lower() or "vektor" in srv.get("name", "").lower():
                print("Found match:", srv)
    else:
        print("Status code:", r.status_code)
except Exception as e:
    print(e)
