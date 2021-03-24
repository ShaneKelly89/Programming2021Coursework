  
import json
# the array we store everything in 
filename="students.json"
students = []

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

writeDict(students)

