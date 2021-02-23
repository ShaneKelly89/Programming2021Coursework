#This is a program that asks the user to input any positive integer
#and outputs the successive values of a calculation 



number = int(input("enter a positive integer: ")) 
print(number)
#I now need to do calculations until the value is equal to 1. 

numberToStop = 1 #Coding for 1 
while number != numberToStop:
    if (number % 2) == 0: 
        number = number / 2 #Here i am dividing even numbers by 2 as per statement 
    else:      #Can only be odd or even 
        number = (number * 3) + 1 #Again I am assigning new value to number to x3 +1 
    #print statement to be placed at this line as we want it to show the new value number within the loop 
    print(int(number))
#Found output presenting as float when ran as print(number) so I will cast it to be an integer



