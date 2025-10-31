# Multiple Inheritance Example
class Base1:
    def feature1(self):
        print("Feature 1 from Base1")

class Base2:
    def feature2(self):
        print("Feature 2 from Base2")

class Child(Base1, Base2):
    def feature3(self):
        print("Feature 3 from Child")

c = Child()
c.feature1()
c.feature2()
c.feature3()