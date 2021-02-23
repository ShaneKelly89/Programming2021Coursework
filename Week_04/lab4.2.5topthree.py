#This program generates 10 random numbers
#prints them out then prints out the top 3 

#a list will be used to store and manipulate the numbers 

import random 
howMany = 10
topHowMany = 3
rangeFrom = 0 
rangeTo = 100

numbers = []

for i in range(0,10):
   numbers.append(random.randint(rangeFrom,rangeTo))
print ("{} random number\t {}".format(howMany,numbers))

#Idea to sort and split the list from stackover flow
#https://stackoverflow.com/questions/32296887/how-to-find-the-1st-2nd-3rd-highest-values-in-a-list-in-python

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))
