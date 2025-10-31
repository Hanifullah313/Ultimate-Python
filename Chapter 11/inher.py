# inheritance example
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"
dog = Dog()
print(dog.speak())  # inherited method
print(dog.bark())   # own method

# anathor example
class Vehicle:
    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def drive(self):
        return "Car is driving"

car = Car()
print(car.start())  # inherited method
print(car.drive())  # own method


# complex example
class Engine:
    def start(self):
        return "Engine started"

class ElectricCar(Car):
    def charge(self):
        return "Car is charging"

tesla = ElectricCar()
print(tesla.start())  # inherited method
print(tesla.drive())  # inherited method
print(tesla.charge())  # own method