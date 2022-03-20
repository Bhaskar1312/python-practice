
class Employee:
    def greet(self):
        print("Employee greet")

class Person:
    def greet(self):
        print("Person greet")

class Manager(Person, Employee):
    pass

manager = Manager()
manager.greet() # Person greet, since it was given first, lookup stops there