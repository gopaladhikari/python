class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def print_full_name(self):
        return f"{self.brand} : {self.model}"

    def fuel_type(self):
        return "Petrol"


class ElectricCar(Car):
    def __init__(self, model, brand, battery):
        super().__init__(model, brand)
        self.battery = battery

    def fuel_type(self):
        return "Electric"


tesla = ElectricCar("Model S", "Tesla", 100)
BMW = Car("X5", "BMW")


print(tesla.fuel_type())
print(BMW.fuel_type())
