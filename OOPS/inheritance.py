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

