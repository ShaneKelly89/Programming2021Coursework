#Write a function that will read in a dict object from file 
#Author Shane Kelly 

import json
filename="testdic.json"

def readDict():
    with open(filename) as f:
        return json.load(f)

somedict = readDict()
print(somedict)