# In these section we will understand about
# Numbers in python, type conversion,Mathematics etc.

#Numbers in python

num1=5
print(num1,"is type of:",type(num1))

num2=3.5
print(num2,"is type of:",type(num2))

num3=8+2j
print(num3,"is type of:",type(num3))

# Type conversion in python

print(type(1+2.5))  #implicit type conversion

num4=int(2.3)       #explicit conversion
print(type(num4))

num5=float(5)       #explicit int to float
print(type(num5))

num6=complex('3+4j')  #explicit string to complex number
print(type(num6))


# Important-python random module

import random

print(random.randrange(10,24)) #it selects any one int value between the given range.

list1=['a','b','c','d','e']
print(random.choice(list1)) #get random item from list.

random.shuffle(list1) #shuffles the list

print(list1)

print(random.random()) #print any random element between 0 and 1.

# Python mathematics

import math

print(math.pi)   #prints value of pi
print(math.cos(math.pi))

print(math.exp(10))

print(math.log(1000))

print(math.sinh(1))

print(math.factorial(4))

