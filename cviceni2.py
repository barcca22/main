class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() +  f"Balík má hodnotu hodnotu {self.value} Kč."
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "doručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]
total_value = 0
for package in package_list:
    if hasattr(package, "value"):
        total_value += package.value
print(f"Celková hodnota balíků je {total_value} Kč.")

total_value_alt = 0
for package in package_list:
    if isinstance(package, ValuablePackage):
        total_value_alt += package.value
print(f"Celková hodnota balíků je {total_value_alt} Kč.")

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() +  f"Balík má hodnotu hodnotu {self.value} Kč."
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "doručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]
total_value = 0
for package in package_list:
    if hasattr(package, "value") and package.state == "nedoručen":
        total_value += package.value
print(f"Celková hodnota balíků je {total_value} Kč.")

class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def get_time_to_read(self):
        pass    
class Book(Item):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages
    def get_info(self):
        return f"Kniha '{self.title}' má {self.pages} stran a stojí {self.price} Kč."
    def get_time_to_read(self):
        return self.pages * 4 / 60
class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator
    def get_time_to_read(self):
        return self.duration_in_hours
favourite_narrator = "Zbyšek Horák"
item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
item_2 = Book("Kadet Hornblower", 399, 242)
item_3 = AudioBook("Odysseus", 389, 13.7, "Lukáš Hlavica")

all_items = [item_1, item_2, item_3]
for item in all_items:
    if hasattr(item, "narrator") and item.narrator == favourite_narrator:
        print(item.title)