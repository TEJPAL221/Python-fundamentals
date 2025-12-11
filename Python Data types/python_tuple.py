# Tuple is similar to the list in python.
# Only diffrence is ,it is immutable.
# We use normal brackets () to represent the tuple.
numbers=(1,2,-5)
tuple_constructor= tuple(('jack','maria','david'))
empty_tuple=()

# Tuples are immutable,ordered,allow duplicates.

# accessing the tuple items.

languages=('python','swift','java','c++')
print(languages[0])
print(languages[2])

 # languages[2]='c' # it will give error
print(len(languages))

# Iterating the list items

for lang in languages:
    print(lang)

# in operator in python

colors=('red','green','yellow','purple')
print('yellow' in colors)  #return True
print('blue' in colors)    #return False

# deleting tuples

del colors
# print(colors)
