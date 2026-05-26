import os
import requests
import json
url = "https://api.dataforsyningen.dk/rest/services"
token = os.getenv("DATAFORSYNINGEN_TOKEN")
if not token:
    raise SystemExit("Missing DATAFORSYNINGEN_TOKEN in environment")
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
