# - Extend Car into an ElectricCar subclass with battery capacity
# Base class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        return f"Car: {self.brand} {self.model}"

# Subclass (Child class)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call parent constructor
        self.battery_capacity = battery_capacity  # New feature

    def electric_info(self):
        return f"{self.car_info()}, Battery: {self.battery_capacity} kWh"

# Create object
my_ev = ElectricCar("Tesla", "Model 3", 75)

# Output
print(my_ev.car_info())        # From parent class
print(my_ev.electric_info())   # From child class
