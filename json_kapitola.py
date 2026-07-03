import json
hours = {"po": 8, "ut": 7, "st": 6, "ct": 5, "pá": 4}
with open("hours.json", "w", encoding="utf-8") as file:
    json.dump(hours, file, ensure_ascii=False)