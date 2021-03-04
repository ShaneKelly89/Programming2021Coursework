# Write a program that takes a positive floating-point number as input and outputs an 
# approximation of its square root.
#First, I must create the function for square root, using newtons method for estimating square roots 
#This was firstly done on a seperate program named 'funtion.py'
#I will then write to code to allow the user to enter the number and along with output print

number = float(input("Please enter a positive number: "))

#How to write code for Newtons method was found using the below link
#https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

def sqRt(value, number_iters = 10):
    a = float(value)  
    for i in range(number_iters):
        value = 0.5 * (value + a / value)
        print(value)
    return value 

print("The square root of {} is approx. {}".format(number, sqRt(number)))