class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def battery_info(self):
        print(f"Capacity: {self.capacity}")


class Engine:
    def __init__(self, power):
        self.power = power

    def engine_info(self):
        print(f"Power: {self.power}")


class ElectricCar(Battery, Engine):
    def __init__(self, model, brand, battery, power):
        Battery.__init__(self, battery)
        Engine.__init__(self, power)
        self.brand = brand
        self.model = model


my_car = ElectricCar("Q3", "Audi", 100, 200)
my_car.battery_info()
my_car.engine_info()
