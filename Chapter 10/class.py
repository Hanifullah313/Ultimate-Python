class Employee :
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show_details(self):
        # why we pass self ?
        # In Python, 'self' refers to the instance of the class. It is used to access variables and methods associated with the current object.
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")



emp1 = Employee("Alice", 30, 70000)
emp2 = Employee("Bob", 25, 50000)

# emp1.show_details()
# emp2.show_details()


class Emp :
    name = "Hanif"
    age = 24
    salary = 60000
    print(f"name is {name}, age is {age}, salary is {salary} ")


emp = Emp()
# print(emp.name)
# print(emp.age)
# print(emp.salary)
emp = Emp()
emp.name = "Ullah"
emp.age = 26
emp.salary = 65000
print(f"name is {emp.name}, age is {emp.age}, salary is {emp.salary} ")