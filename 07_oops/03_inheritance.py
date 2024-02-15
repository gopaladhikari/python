class Car:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    def print_full_name(self):
        return f"{self.brand} : {self.model}"


class ElectricCar(Car):
    def __init__(self, model, brand, battery):
        super().__init__(model, brand)
        self.battery = battery


my_tesla = ElectricCar("Model S", "Tesla", 100)
print(my_tesla.print_full_name())
print(my_tesla.battery)
