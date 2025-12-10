#if-else(flow control) in python
#Note- in python main role is to manage identation

#example-1
number=int(input('Enter a number'))
if number>0:
    print("{} is a positive number",number)
else:
    print("entered number is negative")
    
#example-2(Nested if statement)
if number>=0:
    if number==0:
        print("Given number is zero")
    else:
        print("Given number is positive")
else:
    print("given number is negative")

#example-3(compact if statement)
if number>0:print('positive')
