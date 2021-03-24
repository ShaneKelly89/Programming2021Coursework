import json
students= []
filename="students.json"
def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)
