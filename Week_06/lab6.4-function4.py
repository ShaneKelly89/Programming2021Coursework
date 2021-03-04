#This part of the program will allow program to keep reading the modules until the user a module
#name of blank. 

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"] =int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit:").strip()

    return modules 


