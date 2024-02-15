class Car:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

    def full_name(self):
        return f"{self.brand} : {self.model}"


myCar = Car("Toyota", "Corola")

print(myCar.full_name())
