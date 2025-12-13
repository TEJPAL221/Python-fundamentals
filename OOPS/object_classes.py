# Object and Classes

class Bike:
    name=""
    gear=0
bike1=Bike()

bike1.name="Mountain Bike"
bike1.gear

print(bike1.name)
print(bike1.gear)

bike2=Bike()
bike2.gear=12
bike2.name="kawasaki"

print(f"Name: {bike2.name}, Gears: {bike2.gear}")

# Methods in python

class Room:
    length=0.0
    breadth=0.0
    def calculate_area(self):
        print("Area of room =",self.length*self.breadth)

study_room=Room()

study_room.length=23.4
study_room.breadth=34.5

study_room.calculate_area()

# python constructors

class Car:
    def __init__(self,name=""):
        self.name=name

car1=Car()
car1=Car('hyundai')


