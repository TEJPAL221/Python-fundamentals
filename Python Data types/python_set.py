#Set is collection of unique data,duplicates not allowed.
#Set also allows mixed data types
#Set data structure uses {} curly braces.

#creating sets

student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

empty_set={} #it acutally creates an empty dictionary.
empty_set1=set() #it actually create an empty set.

print(type(empty_set))
print(type(empty_set1))

numbers={2,4,6,8,4,2,8}
print(numbers) # we didnt find any duplicates in output.

# Adding items in set
numbers.add(32)
numbers.add(43)

# updating sets in python
#note - it also

companies = {'Lacoste', 'Ralph Lauren'}  #set
tech_companies = ['apple', 'google', 'apple']  #list

companies.update(tech_companies)
print(companies)

companies.discard('apple') # it removes element from the set
print(companies)

#Iterating over lists.

for company in companies:
    print(company)

print(len(companies))# number of elemets in set.

#Set operations in python

#union
A = {1, 3, 5}
B = {0, 2, 4}

print('Union using |:',A|B)
print('Union using union():',A.union(B))

#Intersection

print('Intersection using &:',A&B)
print('Intersection using intersection():',A.intersection(B))
# Diffrence 

print('Diffrence using &:',A-B)
print('Diffrence using diffrence():',A.difference(B))

# Symmetric diffrence

print('using ^:',A^B)
print('Using symmetric_diffrence():',A.symmetric_difference(B))


# Some other python set methods
'''
Method	                Description
add()	                Adds an element to the set
clear()	                Removes all elements from the set
copy()	                Returns a copy of the set
difference()        	Returns the difference of two or more sets as a new set
difference_update()	    Removes all elements of another set from this set
discard()	            Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()      	Returns the intersection of two sets as a new set
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	        Returns True if two sets have a null intersection
issubset()	            Returns True if another set contains this set
issuperset()	        Returns True if this set contains another set
pop()	                Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	            Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
union()                	Returns the union of sets in a new set
update()	            Updates the set with the union of itself and others

'''
