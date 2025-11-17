class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, {self.num_doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        base_info = super().display_info()
        sidecar_status = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{base_info}, {sidecar_status}"

vehicle1 = Vehicle("Toyota", 2012)
car1 = Car("Tesla", 2023, 4)
motorcycle1 = Motorcycle("Yamaha", 2022, True)
motorcycle2 = Motorcycle("kawasaki", 2021, False)

print(vehicle1.display_info())
print(car1.display_info())
print(motorcycle1.display_info())
print(motorcycle2.display_info())