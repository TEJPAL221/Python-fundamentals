# Strings in python-

string1='python string type 1'
string2="python string type 2"
print(type(string1))
print(type(string2))

# Accessing string characters in python

greet='hello'
print(greet[1])
print(greet[-3])
print(greet[1:4])

# Python strings are also immutable.

greet[2]='d' # it will give error

# Python multiline string

message="""
hello bro how are you?
 I am coming on next monday.
"""
print(message)

#String operation in python

str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"
print(str1==str2) # compare operator

result=str1+str2 #join two strings.

# Iterating list in python

for char in result:
    print(char)
print(len(result))

#Membership operators in string
print('a' in 'program')
print('h' not in result)

#Escape sequence character in strings.
example="he said,\"what's there?\""
example2='he said,"whats\' there?"'

print(example)
print(example2)

'''
Escape Sequence	     Description
\\	                 Backslash
\'                 	 Single quote
\"	                 Double quote
\a	                 ASCII Bell
\b	                 ASCII Backspace
\f	                 ASCII Formfeed
\n	                 ASCII Linefeed
\r	                 ASCII Carriage Return
\t	                 ASCII Horizontal Tab
\v	                 ASCII Vertical Tab
\ooo	             Character with octal value ooo
\xHH	             Character with hexadecimal value HH
'''
#Methoda for python string
'''
Methods         	Description
upper()         	Converts the string to uppercase
lower()         	Converts the string to lowercase
partition()	        Returns a tuple
replace()	        Replaces substring inside
find()	            Returns the index of the first occurrence of substring
rstrip()        	Removes trailing characters
split()         	Splits string from left
startswith()    	Checks if string starts with the specified string
isnumeric()	        Checks numeric characters
index()	            Returns index of substring
'''
