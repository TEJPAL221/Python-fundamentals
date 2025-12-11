#python non-local variables in functions

def outer():
    message='local'
    
    def inner():
        nonlocal message
        message='nonlocal'
        print('inner:',message)
    inner()
    print("outer:",message)
    
outer()

#global variables in python functions

c=1
def add():
    c=c+2     #it will give error ,because we can only access but not modify
    print(c)
add() 

d=1
def increment():
    global c
    c=c+2
    print(c)
increment()  # now it will run easily

# Recursion in python

def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))

num=3
print('the factorial of',num,'is',factorial(num))

