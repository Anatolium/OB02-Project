class Car:
    def __init__(self, make, model):
        self.public_make = make
        self._protected_model = model
        self.__private_year = 2022

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}"

    def _protected_method(self):
        return f"Это защищенный метод"

    def __private_method(self):
        return f"Это приватный метод"

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        details = f"{self.public_make} {self._protected_model}, Батарея: {self.battery_size} kWh"
        return details

tesla = ElectricCar("Tesla", "Model S", 100)

print("public_make =", tesla.public_make)
print(tesla.public_method())

# print("Year:", tesla.__private_year)
print(f"Year: {tesla._Car__private_year}")
