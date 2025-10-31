# Multi Level Inheritance Example
class GrandParent:
    def feature1(self):
        print("Feature 1 from GrandParent")

class Parent(GrandParent):
    def feature2(self):
        print("Feature 2 from Parent")

class Child(Parent):
    def feature3(self):
        print("Feature 3 from Child")

c = Child()
c.feature1()
c.feature2()
c.feature3()



# What is Super() in Python?
# super() is a built-in function in Python that allows you to call methods from a parent class. It is commonly used in inheritance to access methods and properties of a superclass from a subclass.
class A:
    def show(self):
        print("Class A Show Method")

class B(A):
    def show(self):
        super().show()
        print("Class B Show Method")

b = B()
b.show()


# class method 
class Person:
    species = "Homo sapiens"  # class variable

    @classmethod
    def get_species(cls):
        return cls.species
c = Person()
c.get_species()