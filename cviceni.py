class package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg. Jeho stav je {self.state}."

    def delivery_price(self):
        if self.weight <= 5:
            return 100
        elif self.weight <= 20:
            return 200
        else:
            return 500
        
    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen."
        else:
            self.state = "doručen"
            return "Balík uložen."

balik_1 = package("Praha 1, Václavské náměstí 1", 3, "doručen")
balik_2 = package("Brno, náměstí Svobody 5", 15, "nedoručen")
print(balik_1)
print(balik_1.deliver())
print(balik_2)
print(balik_2.deliver())


