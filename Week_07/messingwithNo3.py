#Program which will use messingwithNo & messingwithNo2 to count how many times the program has been run
#Author Shane Kelly 

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number 

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

num = readNumber()
num += 1 
print ("we have run this program {} times".format(num))
writeNumber(num)