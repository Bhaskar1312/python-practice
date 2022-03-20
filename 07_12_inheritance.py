class Animal:
    def __init__(self):
        self.age=1
    def get_age(self):
        print("age", self.age)
    def eat(self):
        print("eat")

class Mammal(Animal): 
    def __init__(self): # method overriding
        super().__init__() # call super constructor, ow, it wont call
        self.weight=10
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

animal = Animal()
animal.eat()
mammal = Mammal()
mammal.eat()
mammal.walk()
fish = Fish()
fish.eat()
fish.swim()
fish.get_age()

print(isinstance(fish, Fish))
print(isinstance(fish, Animal))
print(isinstance(fish, object))

print("SubClass", issubclass(Mammal, Animal))
print("SubClass", issubclass(Mammal, object))

print("mammal age", mammal.age) # gives err without super class' constructor
print("mammal wt", mammal.weight)