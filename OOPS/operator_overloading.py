# Operator overloading

# this feature in python allows the same operator to have diffrent meanings.

num1=5
num2=num1.__add__(5)
print(num2)

'''

Function	        Description
__init__()	        Initialize the attributes of the object.
__str__()	        Returns a string representation of the object.
__len__()	        Returns the length of the object.
__add__()	        Adds two objects.
__call__()	        Call objects of the class like a normal function.
'''

#example-1

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def add_points(self,other):
        x=self.x + other.x
        y=self.y + other.y
        return Point(x,y)
    
p1=Point(1,2)
p2=Point(3,4)

p3=p1.add_points(p2)

print((p3.x,p3.y))

'''

Operator	        Expression	        Internally
Addition	        p1 + p2	            p1.__add__(p2)
Subtraction	        p1 - p2	            p1.__sub__(p2)
Multiplication	    p1 * p2         	p1.__mul__(p2)
Power           	p1 ** p2	        p1.__pow__(p2)
Division	        p1 / p2         	p1.__truediv__(p2)
Floor Division  	p1 // p2	        p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2         	p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	        p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	        p1.__rshift__(p2)
Bitwise AND	        p1 & p2	            p1.__and__(p2)
Bitwise OR	        p1 | p2         	p1.__or__(p2)
Bitwise XOR	        p1 ^ p2         	p1.__xor__(p2)
Bitwise NOT	        ~p1	                p1.__invert__()

'''

# example2

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __lt__(self,other):
        return self.age<other.age
    
person1=Person("Alice",30)
person2=Person("Bob",32)

print(person1<person2)
print(person1>person2)
        
'''


Operator	                Expression	        Internally
Less than               	p1 < p2         	p1.__lt__(p2)
Less than or equal to	    p1 <= p2	        p1.__le__(p2)
Equal to	                p1 == p2	        p1.__eq__(p2)
Not equal to	            p1 != p2        	p1.__ne__(p2)
Greater than	            p1 > p2         	p1.__gt__(p2)
Greater than or equal to	p1 >= p2	        p1.__ge__(p2)

'''

