import logging
from random import randint

logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w", format="%(asctime)s - %(filename)s:%(lineno)d  %(funcName)s() - %(message)s")

def hra():
    logging.debug("Začátek hry")
    sazka = float(input("Zadejte sázku: "))
    tip = int(input("Tipujte sudý nebo lichý součet (0 pro sudý, 1 pro lichý): ").lower())
    logging.debug(f"Sázka: {sazka}, Tip: {tip}")

    kostka1 = randint(1, 6)
    kostka2 = randint(1, 6)
    kostka3 = randint(1, 6)

    soucet = kostka1 + kostka2 + kostka3
    
    logging.info(f"Výsledek hodu: {kostka1}, {kostka2}, {kostka3} - Součet: {soucet}")
    if (tip == 0 and soucet % 2 == 0) or (tip == 1 and soucet % 2 == 1):
        vyhra = sazka * 2
        logging.info(f"Výhra: {vyhra}")
        print(f"Vyhráli jste! Váš výherní obnos je: {vyhra}")
    else:
        logging.info("Prohra")
        print("Bohužel, prohráli jste.")
    logging.debug("Konec hry")
if __name__ == "__main__":
    hra()