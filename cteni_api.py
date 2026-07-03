import json
import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()
data.pop("length")
with open("catfact.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

