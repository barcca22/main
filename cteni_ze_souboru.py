lines = []
vykazy = []

with open('vykaz.txt', encoding='utf-8') as file:
    for line in file:
        vykazy.append(float(line))

hodinova_mzda = int(input("Napiš hodinovou mzdu v Kč: "))
celkova_mzda = 0
    
for vykaz in vykazy:
    celkova_mzda += hodinova_mzda * vykaz
    
print(celkova_mzda)
print(celkova_mzda / len(vykazy))

rates = {"Polcoin": 0.47, "PyCoin": 0.21, "Czechitacoin": 0.13}
total_usd = 0
with open("transaction_list.csv", encoding="utf-8") as file:
    for line in file:
        transaction_date, value_str, currency = line.split(";")
        # množství kryptoměny jako číslo
        amount = float(value_str)
        # název měny bez \n na konci
        crypto = currency.strip()
        # kurz dané měny
        rate = rates[crypto]
        # přičtu hodnotu této transakce v dolarech
        total_usd += amount * rate
# převedu na celé dolary (můžeš použít int nebo round)
print(f"Hodnota úspor Markéty je {total_usd} dolarů.")

total_usd= round(total_usd)
print(f"Hodnota úspor Markéty je {total_usd} dolarů.")

text = ["Tatiana", "Klára", "Markéta", "Pavla", "Jana"]

with open("soubory/soubor.txt", "w", encoding="utf-8") as output_file:
    for item in text:
        print(item, file=output_file)

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
with open("soubory/kalendar.txt", "w", encoding="utf-8") as output_file:
    for pocet in pocty_dni:
        print(pocet, file=output_file)

file_name = input("Zadej název souboru: ")
text = input("Zadej text: ")

with open(file_name, mode="w", encoding="utf-8") as output_file:
    print(text, file=output_file)