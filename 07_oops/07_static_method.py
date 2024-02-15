class Car:
    total = 0

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        Car.total += 1

    @staticmethod
    def general_description():
        return "Car are awesome"


tesla = Car("Model S", "Tesla")

print(Car.general_description())
