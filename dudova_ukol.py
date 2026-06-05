from math import ceil
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    coefficient = { "land": 0.85, "building site": 0.9, "forrest": 0.35, "garden": 2.5 }

    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        tax = self.area * self.coefficient.get(self.estate_type, 0) * self.locality.locality_coefficient
        return ceil(tax)

class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            tax *= 2
        return tax

# Testovací data
manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

#Zemědělský pozemek v Manětíně o rozloze 900 m2
estate = Estate(manetin, "land", 900)
print(f"Daň z zemědělského pozemku v Manětíně: {estate.calculate_tax()} Kč")

#Dům v Brně o rozloze 120 m2
house = Residence(manetin, 120)
print(f"Daň z domu v Manětíně: {house.calculate_tax()} Kč")

#Kancelář v Brně o rozloze 90 m2
office = Residence(brno, 90, commercial=True)
print(f"Daň z kanceláře v Brně: {office.calculate_tax()} Kč")
