#This is a program which stores a students name and a list of her courses and grades 
#the program will also print out her data 
#The number of courses she has could change 
#Author Shane Kelly

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade": 99
        }
    ]
} 

print ("Student: {}".format(student["name"]))
for module in student ["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
