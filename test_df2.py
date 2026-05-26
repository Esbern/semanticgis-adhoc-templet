import os
import requests
import xml.etree.ElementTree as ET

urls_to_test = [
    "https://api.dataforsyningen.dk/geodanmark_60_vektor/wfs",
    "https://services.datafordeler.dk/GeoDanmarkVector/GeoDanmark60_GML2/1.0.0/WFS",
    "https://services.datafordeler.dk/GeoDanmarkVector/GeoDanmark60_GML3/1.0.0/WFS",
    "https://services.datafordeler.dk/GeoDanmark/GeoDanmark60/1.0.0/WFS"
]

token = os.getenv("DATAFORSYNINGEN_TOKEN")
if not token:
    raise SystemExit("Missing DATAFORSYNINGEN_TOKEN in environment")

params_token = {
    "service": "WFS",
    "request": "GetCapabilities",
    "token": token,
}

for url in urls_to_test:
    try:
        r = requests.get(url, params=params_token)
        print(f"URL: {url} -> Status: {r.status_code}")
        if r.status_code == 200:
            print(r.text[:200])
    except Exception as e:
        pass

