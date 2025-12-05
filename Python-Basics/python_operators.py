#Arithmetic operators

a=2+5     #addition operator
b=5-4     #subtraction operator
c=5*4     #multiplication operator
d=10/2    #division operator
e=10//3   #floor division operator
f=10**2   #power operator
g=10%4    #modulo operator

#Assignment operators

a = 7  # Assignment Operator
a += 1 # Addition Assignment
a -= 3 # Subtraction Assignment
a *= 4 # Multiplication Assignment
a /= 3 # Division Assignment
a %= 10 # Remainder Assignment
a **= 10 # Exponent Assignment

#Comparison operator(answers in boolean value)

a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

# Python Logical Operators

a = 5
b = 6

print((a > 2) and (b >= 6))

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

#Identity operators

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False

#Membership Operators

message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False

##Operator precedence
'''
Operators	        Meaning
()      	        Parentheses
**	                Exponent
+x, -x, ~x	        plus, Unary minus, Bitwise NOT
*, /, //, %	        Multiplication, Division, Floor division, Modulus
+, -	            Addition, Subtraction
<<, >>	            Bitwise shift operators
&               	Bitwise AND
^               	Bitwise XOR
|               	Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators
not	                Logical NOT
and	                Logical AND
or	                Logical OR
'''
