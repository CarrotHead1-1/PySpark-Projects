import requests
import pandas as pd

#API's
API_KEY = ''


url = f"https://api.tfl.gov.uk/StopPoint/Mode/tube?app_key{API_KEY}"

res = requests.get(url)
data = res.json()

stations = []
for stop in data["stopPoints"]:
    stations.append({
        "id": stop["id"],
        "name": stop["commonName"],
        "lat": stop["lat"],
        "lon": stop["lon"],
        "modes": stop["modes"],
        "zone": next((p["value"] for p in stop["additionalProperties"] if p["key"] == "Zone"), None)
    })

df = pd.DataFrame(stations)
df.to_csv("tflStations.csv", index=False)

