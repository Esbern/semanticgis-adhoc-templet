import requests
url = "https://services.datafordeler.dk/GeoDanmarkVector/GeoDanmark60_GML3/1.0.0/WFS"
params = {
    "service": "WFS",
    "request": "GetCapabilities",
    "username": "81512860b82d0f1a8814a5775e088ba4",
    "password": "81512860b82d0f1a8814a5775e088ba4"
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
    "token": "81512860b82d0f1a8814a5775e088ba4"
}
try:
    r = requests.get(url2, params=params2)
    print("Status code (token):", r.status_code)
except Exception as e:
    print(e)
