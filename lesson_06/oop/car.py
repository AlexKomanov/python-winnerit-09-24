class Car:
    def __init__(self, name: str, manufacturer: str):
        self.name = name
        self.manufacturer = manufacturer
        print(f"{self.name} by {self.manufacturer} is a car.")

    def drive(self):
        print("The car is driving")


class ElectricCar(Car):
    def __init__(self, name: str, manufacturer: str, battery_capacity: int = 100):
        # קריאה לקונסטרקטור של מחלקת האב
        super().__init__(name, manufacturer)
        self.battery_capacity = battery_capacity
        print(f"{self.name} has a battery capacity of {self.battery_capacity} kWh.")

    def drive(self):
        print("The electric car is driving silently")

    def charge(self):
        print(f"{self.name} is charging...")

    def get_capacity(self):
        print(f"{self.battery_capacity = }")

car = Car("Model 7", "BMW")
car.drive()
my_electric_car = ElectricCar("Model S", "Tesla", )
my_electric_car.drive()
my_electric_car.charge()
my_electric_car.get_capacity()
my_electric_car.battery_capacity = -10
my_electric_car.get_capacity()
