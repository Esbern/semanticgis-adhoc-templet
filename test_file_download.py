import os
import requests

api_key = os.getenv("DATAFORDELER_API_KEY")
if not api_key:
    raise SystemExit("Missing DATAFORDELER_API_KEY in environment")

url = "https://api.datafordeler.dk/FileDownloads/GetFile"
params = {
    "Register": "GeoDanmark",
    "LatestTotalForEntity": "Vejmidte",
    "type": "current",
    "format": "GPKG",
    "apiKey": api_key,
}
try:
    r = requests.get(url, params=params)
    print("Status code:", r.status_code)
    print("Headers:", r.headers)
    if r.status_code == 200:
        print("Success!")
    else:
        print(r.text[:200])
except Exception as e:
    print(e)
