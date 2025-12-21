# List comprehension

numbers=[1,2,3,4]
doubled_numbers=[num*2 for num in numbers]

#syntax-[expression for item in list if condition == true]

squared_numbers=[num*num for num in numbers]

even_numbers=[num for num in range(1,10) if num%2==0]

# list comprehension with string

word="python"
vowels="aeiou"

result=[char for char in word if char in vowels]

#Lambda/anonymous function

greet=lambda : print('Hello World')

greet()

greet_user=lambda name : print('hey there,',name)
greet_user('harry')



my_list=[2,4,67,3,3,6,7,9,12,33]
new_list=list(filter(lambda x: (x%2==0),my_list))
print(new_list)



my_list2=[2,5,8,4,12,33,56,3]
new_list2=list(map(lambda x: x*2 , my_list2))
print(new_list2)

#Iterators

iterator=iter(my_list)
print(next(iterator))
print(next(iterator))

for element in iterator:
    print(element)

#custom iterators

class PowTwo:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
numbers=PowTwo(3)
i=iter(numbers)
print(next(i))

print(next(i))
print(next(i))
print(next(i))

#infinite iterator

from itertools import count

infinite_iterator=count(1)
for i in range(5):
    print(next(infinite_iterator))
