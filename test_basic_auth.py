import requests
from requests.auth import HTTPBasicAuth
url = "https://services.datafordeler.dk/GeoDanmarkVector/GeoDanmark60_GML3/1.0.0/WFS"
params = {
    "service": "WFS",
    "request": "GetCapabilities",
}
auth = HTTPBasicAuth("81512860b82d0f1a8814a5775e088ba4", "81512860b82d0f1a8814a5775e088ba4")
try:
    r = requests.get(url, params=params, auth=auth)
    print("Status code (basic auth GeoDanmark60_GML3):", r.status_code)
except Exception as e:
    print(e)

url2 = "https://services.datafordeler.dk/GeoDanmark/GeoDanmark60/1.0.0/WFS"
try:
    r = requests.get(url2, params=params, auth=auth)
    print("Status code (basic auth GeoDanmark60):", r.status_code)
except Exception as e:
    print(e)
    
url3 = "https://services.datafordeler.dk/GeoDanmark/WFS"
try:
    r = requests.get(url3, params=params, auth=auth)
    print("Status code (basic auth WFS):", r.status_code)
except Exception as e:
    print(e)
