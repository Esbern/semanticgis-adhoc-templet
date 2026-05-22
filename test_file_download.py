import requests

url = "https://api.datafordeler.dk/FileDownloads/GetFile"
params = {
    "Register": "GeoDanmark",
    "LatestTotalForEntity": "Vejmidte",
    "type": "current",
    "format": "GPKG",
    "apiKey": "81512860b82d0f1a8814a5775e088ba4"
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
