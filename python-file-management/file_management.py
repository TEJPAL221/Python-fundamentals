# file management in python

import os
import shutil
print(os.getcwd())  #returns current working directory
os.chdir('C:\Users\tejpal singh rathore\Downloads\Python-practice')#changes current directory to path directory.
os.listdir() #list all sub-directories
os.mkdir('test') #creates new directory
os.rename('test','new_dir') #renames the directory
os.remove('myfile.txt') #deletes the file
os.rmdir('new_dir') # deletes the empty directory
shutil.rmtree("mydir") # for removing non-empty directory

#csv files in python

import csv

# reading csv files

with open('people.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        
# write to csv file in python

with open('protaganist.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["sn","movie","protaganist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])

#writing dictionaries to csv files

with open('players.csv','w',newline='') as file:
    fieldname=['player_name','field_rating']
    writer=csv.DictWriter(file,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
    
# Using pandas to handle csv files

import pandas as pd
pd.read_csv('people.csv')# reading

df=pd.DataFrame([['Jack', 24], ['Rose', 22]], columns = ['Name', 'Age'])
df.to_csv('person.csv')


