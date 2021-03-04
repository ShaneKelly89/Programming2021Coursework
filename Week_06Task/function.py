# Write a program that takes a positive floating-point number as input and outputs an 
# approximation of its square root.
#This is part 1 of this program, where I will create a function used to approximate square root.
#Author Shane Kelly 

def sqRt(number, number_iters = 500):
    a = float(number) #the number we will be getting the square root on 
    for i in range(number_iters):
        number = 0.5 * (number + a / number)
    return number 

print(sqRt(9))