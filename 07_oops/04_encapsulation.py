class Car:
    def __init__(self, model, brand):
        self.model = model
        self.__brand = brand

    def get_brand(self):
        return self.__brand


tesla = Car("Model S", "Tesla")
print(tesla.__brand)
print(tesla.get_brand())
