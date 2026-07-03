import requests

ico = input("Zadej IČO: ")

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
                        
data = response.json()

print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])


import requests
import json

nazev = input("Zadej název firmy: ")

headers = {"accept": "application/json",
    "Content-Type": "application/json",}

data = {"obchodniJmeno": nazev}

response = requests.post(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=json.dumps(data))

vysledek = response.json()

print(f"Nalezeno subjektů: {vysledek['pocetCelkem']}")

for subjekt in vysledek["ekonomickeSubjekty"]:
    print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")
    