# Inheritance in python

# Note-it allows us to create new class from existing one.

class Animal:
    name=""
    def eat(self):
        print("I can eat")
class Dog(Animal):        #we can extend by adding parent class by passing as argument.
    def display(self):
        print("My name is ",self.name)
labrador=Dog()
labrador.name="Rohu"

labrador.eat()
labrador.display()

# Note-inheritance is an is-a relationship.
# car is a vehicle
# apple is a fruit
# cat is an animal

# Method overriding in python inheritance

class Car:
    def drive(self):
        print('i can drive.')
class F1car(Car):
    def drive(self):           # This function will override the parent class drive function.
        super().drive()        #it calls upper class function
        print("I can drive faster.") #it actually overrides.

car1=F1car()
car1.drive()

'''
Inheritance Types-
There are 5 different types of inheritance in Python. They are:

Single Inheritance: a child class inherits from only one parent class.
Multiple Inheritance: a child class inherits from multiple parent classes.
Multilevel Inheritance: a child class inherits from its parent class, which is inheriting from its parent class.
Hierarchical Inheritance: more than one child class are created from a single parent class.
Hybrid Inheritance: combines more than one form of inheritance.
'''

# Multiple inheritance in python
# A class can be derived from more than one superclass in python.

class Mammal:
    def mammal_info(self):
        print("mammals can give direct birth")
class WingedAnimal:
    def winged_animal_info(self):
        print("winged animal can flap")
class Bat(Mammal,WingedAnimal):
    pass
b1=Bat()
b1.mammal_info()
b1.winged_animal_info()

#Multilevel inheritance in python

class SuperClass:

    def super_method(self):
        print("Super Class method called")

class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")


d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"

d2.derived1_method()  # Output: "Derived class 1 method called"

d2.derived2_method()  # Output: "Derived class 2 method called"

# Method resolution order in python

class SuperClass1:
    def info(self):
        print("Super Class 1 method called")

class SuperClass2:
    def info(self):
        print("Super Class 2 method called")

class Derived(SuperClass1, SuperClass2):
    pass

d1 = Derived()
d1.info()  

# Output: "Super Class 1 method called"
