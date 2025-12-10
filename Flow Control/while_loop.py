# While loop in python second most important loop

# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')


age = 32

# The test condition is always True
while age > 18:
    print('You can vote')
