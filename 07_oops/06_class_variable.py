class Car:
    total = 0

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        Car.total += 1

    def print_full_name(self):
        return f"{self.brand} : {self.model}"

    def fuel_type(self):
        return "Petrol"


tesla = Car("Model S", "Tesla")
BMW = Car("Model 3", "BMW")

print(Car.total)
