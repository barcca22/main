class employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def __str__(self):
        return f"Zaměstnanec: {self.name} pracuje na pozici {self.position}."
    
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement = self.holiday_entitlement - days
            return "Užij si to"
        else:
            return f"Bohužel, zbývá ti už jen {self.holiday_entitlement} dní."
   
    def nova_pozice(self, new_position):
        self.position = new_position.upper()

emp_1 = employee("Jan Novák", "programátor", 25)
emp_2 = employee("Petra Svobodová", "grafička", 20)



print(emp_1)
print(emp_2) 