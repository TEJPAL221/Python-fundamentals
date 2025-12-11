# List in python allows us to store diffrent data types.
# It is similar to dynamic arrays
# Lists are ordered,mutable,allows duplicates

# Creating list in python

ages=[12,53,23,56,33] #lists use square brackets
student=['jack',32,'computer science']
empty_list=[]

print(ages)
print(student)
print(empty_list)

# Accessing list elements

print(student[2]) #normal indexing like arrays in other languages.
print(ages[2])

print(student[-1]) #negative indexing-starts from right to left.
print(ages[-3])

# Slicing of list in python

my_list=['p','r','0','g','r','a','m']

print(my_list[2:5])  #last index is excluded- 5 in this case
print(my_list[2:-2]) #index 2 to -3 only, -2 is excluded.
print(my_list[2:])   #start from index 2 till end.
print(my_list[: 4]) # from start to 3rd index.
print(my_list[:-3]) #from start to -4 index.
print(my_list[:])   #prints whole list.

# Adding elements in list

my_list.append('y')   #adds element at the last of the list.
my_list.insert(3,'x') # add element at the specified position in list.

numbers=[1,3,5,6]
even_numbers=[2,4,6,8]

numbers.extend(even_numbers) # extends the list.
print(numbers)

# updating the list(update,remove,delete)

colors=['Red','Black','Blue','Green']
colors[2]='Purple' #updated list item

print(colors)

colors.remove('Red') #Note-python is case sensitive language ('Red' and 'red' are treated as diffrent)
print(colors)

del my_list[3] # it deletes the item at 3 index.
print(my_list)
del colors     # it deletes the full list
print(colors)
del my_list[2:4] #delete from index 2 to 3

print(len(my_list)) # len() function in python returns length of list.

# Iterating in list

for i in my_list:
    print(i)

# some important functions of list
'''
Method	    Description

append()	Adds an item to the end of the list
extend()	Adds items of lists and other iterables to the end of the list
insert()	Inserts an item at the specified index
remove()	Removes the specified value from the list
pop()	    Returns and removes item present at the given index
clear()   	Removes all items from the list
index()	    Returns the index of the first matched item
count()	    Returns the count of the specified item in the list
sort()	    Sorts the list in ascending/descending order
reverse()	Reverses the item of the list
copy()	    Returns the shallow copy of the list
'''
