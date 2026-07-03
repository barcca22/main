import requests

ico = input("Zadej IČO: ")

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")

if response.status_code == 200:
    data = response.json()

    print(data["obchodniJmeno"])
    print(data["sidlo"]["textovaAdresa"])
else:
    print("Subjekt nebyl nalezen.")

import requests
import json

nazev = input("Zadej název subjektu: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = json.dumps({"obchodniJmeno": nazev})

response = requests.post(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

if response.status_code == 200:
    vysledek = response.json()

    print(f"Nalezeno subjektů: {vysledek['pocetCelkem']}")

    for subjekt in vysledek["ekonomickeSubjekty"]:
        print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")
else:
    print("Při vyhledávání nastala chyba.")