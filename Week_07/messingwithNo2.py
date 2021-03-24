#Program containing a function that takes in a number and overwrites a file with that number 
#Author Shane Kelly 

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

writeNumber(3) 