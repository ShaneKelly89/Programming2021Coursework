#This is a program containing the function that will read in a number from a file that already exists
#Author Shane Kelly

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

num = readNumber
print(num)