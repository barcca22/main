import json
with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)
winner = runners[0]
official_time = winner["casy"]["oficialni"]
print(f"Vítězem závodu se stává {winner['jmeno']} s časem {official_time}.")
print(f"Neoficiální čas vítěze je {winner['casy']['2.kolo']}.")