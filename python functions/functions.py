# Functions in python

#creating functions

def greet():
    print("hello world!")

#calling function

greet()

def greet(name):
    print("hello",name)

greet("john")

def add_numbers(num1,num2):
    sum=num1+num2
    print("sum:",sum)
add_numbers(5,4)

def find_square(num):
    result=num*num
    return result
square=find_square(5)
print('square:',square)

#pass statement in function

def future_function():   #to add implementation later
    pass

import math

square_root=math.sqrt(4)
print(square_root)

power=pow(2,6)
print(power)

def greet(name,message='hello'):
    print(message,name)    # hello is by default value

greet("alice","good morning")

greet("bob")

#python keyword argument

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')

#python function with arbitrary arguments

def find_sum(*numbers):   # we can pass any number 
    result=0
    for num in numbers:
        result=result+num
        
    print('sum= ',result)

find_sum(1,2,3,4)

