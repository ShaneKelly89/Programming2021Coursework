#Give the absolute value of the number
#Author Shane Kelly

#In the question, number is ambiguos but the output implies that we should 
#be dealing with floats so I am casting the input to a float 

number= float(input("Enter a number:"))
absoluteValue = abs(number)

print('The absolute value of {} is{}'.format(number, absoluteValue))
