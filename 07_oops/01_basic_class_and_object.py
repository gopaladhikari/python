class Car:
    brand = ""
    model = ""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corola")

print(my_car.brand)
print(my_car.model)


my_new_car = Car("BMW", "X5")
print(my_new_car.brand)
print(my_new_car.model)
