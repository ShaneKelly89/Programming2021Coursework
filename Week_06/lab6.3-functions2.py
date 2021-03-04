#this is the second part of the larger overall program 
#this part of the program use the function from lab6.2, and will now continue to display the menu
#until the user selects 'q'. 
#When selecting A - the a function called doAdd() will be called.
#When selecting V - the function called doView() will be called. 
#Author Shane Kelly

def displayMenu():
    print ("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice 
def doAdd():
    print("in adding")
def doView():
    print("in viewing")

#main program 
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()

