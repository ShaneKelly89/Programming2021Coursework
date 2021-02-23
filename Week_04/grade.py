#This is a program that reads in a students percentage mark and prints out corresponding grade
#Author Shane Kelly

percentage = float(input("Enter the percentage: "))
#print (percentage)

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 40: 
    print ("Fail")
elif percentage < 50: #(between 40 and 49)
    print ("Pass")
elif percentage < 60: #(50 to 59)
    print ("Merit1")
elif percentage < 70: #60 to 69
    print ("Merit2")
else: # 70 tp 100
    print ("Distinction")
    