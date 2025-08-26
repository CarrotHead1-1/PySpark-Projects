
import requests
import pandas as pd 

OVERPASS_URL = "http://overpass-api.de/api/interpreter"

query = """ 
[out:json];
area(3600175342) ->.searchArea;
(
    node["amenity"="cafe"](area.searchArea);
    way["amenity"="cafe"](area.searchArea);
    relation["amenity"="cafe"](area.searchArea);
    );
    out center;
"""

res = requests.get(OVERPASS_URL, params={'data': query})
data = res.json()

#Parse JSON file into a list of cafes
cafes = []
for element in data['elements']:
    cafe = {
        "id": element["id"],
        "lat": element.get("lat", element.get("center", {}).get("lat")),
        "lon": element.get("lon", element.get("center", {}).get("lon")),
        "name": element['tags'].get("name", "Unknown"),
        "street": element["tags"].get("addr:street", None),
        "postcode": element["tags"].get("addr:postcode", None),
        "brand": element["tags"].get("brand", None)
    }
    cafes.append(cafe)

df = pd.DataFrame(cafes)
print(df.head())
df.to_csv("osmCafeLondon.csv", index=False)
