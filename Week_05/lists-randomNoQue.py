#This is program that puts ten random numbers in a a queue that will first output all values in the queue
#It will then take the numbers from the queue one at a time, print it and the current numbers still in the Q
#Author Shane Kelly 


import random 
queue = []
numberOfNumbers = 10 
rangeTo = 100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print ("queue is {}".format(queue))

while len(queue) != 0:
    
    currentNumber = queue.pop(0)
    print ("current Number is {} and the queue is {}".format(currentNumber, queue))

print ("the queue is now empty")