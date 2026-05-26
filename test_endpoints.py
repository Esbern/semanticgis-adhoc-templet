import os
import requests

urls = [
    "https://api.dataforsyningen.dk/fot_vektor/wfs",
    "https://api.dataforsyningen.dk/FOT/wfs",
    "https://api.dataforsyningen.dk/GeoDanmark_60/wfs",
    "https://api.dataforsyningen.dk/geodanmark/wfs",
    "https://api.dataforsyningen.dk/wfs"
]
token = os.getenv("DATAFORSYNINGEN_TOKEN")
if not token:
    raise SystemExit("Missing DATAFORSYNINGEN_TOKEN in environment")

for url in urls:
    try:
        r = requests.get(url, params={"request": "GetCapabilities", "service": "WFS", "token": token})
        print(f"URL: {url} -> Status: {r.status_code}")
    except Exception as e:
        pass
