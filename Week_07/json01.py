#Using json module for the first time 
#Json can be used to store more complicated data structures and store them in a readable way
#This program will hold a function which stores a simple Dict to a file as JSON
#Author Shane Kelly 

import json
filename = "testdic.json"
sample = dict(name='fred', age=31, grades= [1,34,55])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

writeDict(sample)