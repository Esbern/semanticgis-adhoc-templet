import requests

urls = [
    "https://api.dataforsyningen.dk/fot_vektor/wfs",
    "https://api.dataforsyningen.dk/FOT/wfs",
    "https://api.dataforsyningen.dk/GeoDanmark_60/wfs",
    "https://api.dataforsyningen.dk/geodanmark/wfs",
    "https://api.dataforsyningen.dk/wfs"
]
token = "h9b5nJDYLX92VF2YC3Jf7IM2a6U5f5nXXgkFXhQkXNSZtYJ1xLomdiS0gFo9VF5TUBmPQi5UfCHqeO7OmPh79batxhXda3zgM"

for url in urls:
    try:
        r = requests.get(url, params={"request": "GetCapabilities", "service": "WFS", "token": token})
        print(f"URL: {url} -> Status: {r.status_code}")
    except Exception as e:
        pass
