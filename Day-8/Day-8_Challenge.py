# - Create a Car class with attributes and a display method
class Car:
    def __init__(self,name, model, year):
        self.name =name
        self.model = model
        self.year = year

    def display(self):
        return f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}"
# Create an object named my_car and call the display method
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display())
# Modify the attributes of my_car
my_car.name = "Honda"
my_car.model = "Civic"
my_car.year = 2021
print(my_car.display())
