import requests
import os

# TODO 1: get latitude and longitude
LATITUDE: float = 35.002460
LONGITUDE: float = -5.903560
API_KEY: str = os.environ["OWM_API_KEY"]
OWM_ENDPOINT: str = "https://api.openweathermap.org/data/2.5/onecall"
parameters: dict = {
    "lat": LATITUDE,
    "lon": {LONGITUDE},
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
}

# TODO 2: make a request to the One Call API using the requests module
response = requests.get(OWM_ENDPOINT, params=parameters)

# TODO 3: print out the HTTP status code that you get back
print(f"{response.status_code}\n")

# TODO 4: print the response to the console
# TODO 5: take the next 12 hours data
data = response.json()["hourly"][:12]
print(data)
print(len(data))

rainy_hours = [data[id_item]["weather"][0]["id"] for id_item in range(len(data))
               if int(data[id_item]["weather"][0]["id"]) < 700]

if rainy_hours:
    print("Bring an umbrella.")
    
