#This is a program containing a function that prints out a menu of commands (ie add, view, quit)
#The function should return what the user selects
#Authour Shane Kelly 
#This is the first part of a larger program which will allow users to create new add new students 
#to a list. It will also allow you to view students on the list. 



def displayMenu():
    print ("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice 

choice = displayMenu()
print("you chose {}".format(choice))
