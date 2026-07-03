class Employee:
    def __init__(self, name, position, holiday_entitlement, car):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.car = car
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement, car)
        self.subordinates = subordinates
        self.car = car
class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        super().__init__(name, position, holiday_entitlement, car)
        self.car = car
frantisek = Employee("Frantisek Novák", "zamestnanec", 25, "Škoda Superb")
marian = Manager("Marian Přísný", "vedoucí", 25, 5, "Škoda Octavia") 
marketa = Manager("Markéta Polková", "teamleader", 30, 10, "Audi A4")   
jakub = Salesman("Jakub Dvořák", "obchodník", 20, "Škoda Fabia")   
atribut = input("Zadej atribut, který chceš zobrazit: ")
print(getattr(marian, atribut))