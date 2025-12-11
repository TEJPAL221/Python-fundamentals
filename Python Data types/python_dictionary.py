# Dictionary in python
# Its similar to list only diffrence is it stores in key-value pairs.

#creating a dictionary
country_captials={"Germany":"Berlin","Canada": "Ottawa", "England": "London"}
print(country_captials)

#note-keys of dictionary are immutable.

my_dict={1:'one',2:'two',3:'three'}  #valid
my_dict2={(1,2):"one two",3:"three"} #valid
my_dict3={1:'hello',[1,2]:"hello hi"} #valid
my_dict = {"USA": ["Chicago", "California", "New York"]}

print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"
del country_capitals["Germany"]
print(country_captials)

country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# clear the dictionary
country_capitals.clear()

# print dictionary keys one by one
for country in country_capitals:
    print(country)

# get dictionary's length
print(len(country_capitals)) 

file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)       # Output: True
print(".mp3" in file_types)       # Output: False
print(".mp3" not in file_types)   # Output: True

# Some other important methods
'''
Function	            Description
pop()	                Removes the item with the specified key.
update()	            Adds or changes dictionary items.
clear()	                Remove all the items from the dictionary.
keys()	                Returns all the dictionary's keys.
values()	            Returns all the dictionary's values.
get()	                Returns the value of the specified key.
popitem()	            Returns the last inserted key and value as a tuple.
copy()	                Returns a copy of the dictionary.
'''
