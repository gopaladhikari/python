class Car:
    def __init__(self, model, brand):
        self.__model = model
        self.brand = brand

    @property
    def model(self):
        return self.__model


tesla = Car("Model S", "Tesla")
tesla.__model = "new model"

print(tesla.model)
