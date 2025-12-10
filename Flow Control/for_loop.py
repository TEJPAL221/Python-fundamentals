#For loop most essential part of control-flow

# example-1
languages=['Hindi','English','German']

for lang in languages:
    print(lang)
    
# example-2(iterating a string)

language='python'
for x in language:
    print(x)
    print('|')

# example-3(python range(start,end))

values=range(0,4)     # Note-last number is excluded
for i in values:
    print(i)
    
# example-4 (Break and Continue statement in python)

for lang in languages:
    if lang=='English':
        break
    else:print(lang)

for lang in languages:
    if lang=='German':
        continue
    else: print(lang)
    
# Nested For loops in python

attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']

for attribute in attributes:
    for car in cars:
        print(attribute,'-',car)
    print('----')

# for loop without accessing sequence

items=range(0,3)
for _ in items:
    print("hii")
