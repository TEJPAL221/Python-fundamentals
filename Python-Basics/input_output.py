#Output in python

print("hello bro,")
print("its rainy day today!")

# print statement with end parameter

print("Hello Friend",end=' ') #by default end parameter is set to'\n'.
print("sun is hidden today")

#print statement with separator parameter.
print('New Year',2023,'see you soon!',sep=',,,')

#concatenation
print("hello"+"world")

# formatting
x=10
y=12
print("the value of x is{} and y is {}.".format(x,y))

#Note- no need of comma(,) after object end directly add .format(x,v,..)



# Taking input in python

num=input("Enter a number ") #prompt inside input is not mandatory but good practice.
print(num)
print(type(num))
# By default input is taken into string format. we need to convert it into integer.

num=int(num)
num=num+12
print(num)
