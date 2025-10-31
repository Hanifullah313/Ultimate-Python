# Property methods in Python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * (self._radius ** 2)
c = Circle(5)
print("Radius:", c.radius)        # Accessing radius property
print("Area:", c.area)            # Accessing area property
# what is property methods in python?
# Property methods in Python are a way to manage the attributes of a class. They allow you to define methods in a class that can be accessed like attributes, providing a way to add validation or other logic when getting or setting a value.




# sample example on property methods
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32


t = Temperature(25)
print("Celsius:", t.celsius)            # Accessing celsius property
print("Fahrenheit:", t.fahrenheit)      # Accessing fahrenheit property