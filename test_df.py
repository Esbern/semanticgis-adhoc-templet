import os
import requests

api_key = os.getenv("DATAFORDELER_API_KEY")
if not api_key:
    raise SystemExit("Missing DATAFORDELER_API_KEY in environment")

url = "https://services.datafordeler.dk/GeoDanmarkVector/GeoDanmark60_GML3/1.0.0/WFS"
params = {
    "service": "WFS",
    "request": "GetCapabilities",
    "username": api_key,
    "password": api_key,
}
try:
    r = requests.get(url, params=params)
    print("Status code (user/pass):", r.status_code)
except Exception as e:
    print(e)

url2 = "https://services.datafordeler.dk/GeoDanmarkVector/GeoDanmark60_GML3/1.0.0/WFS"
params2 = {
    "service": "WFS",
    "request": "GetCapabilities",
    "token": api_key,
}
try:
    r = requests.get(url2, params=params2)
    print("Status code (token):", r.status_code)
except Exception as e:
    print(e)
