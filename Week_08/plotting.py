import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints 

#plt.plot(xpoints, ypoints)
#plt.show()

#Write a program that plots a histogram of the salaries
minSal = 20000
maxSal = 80000
numOfEnt = 100

np.random.seed(1)
salaries = np.random.randint(minSal, maxSal, numOfEnt)

#plt.hist(salaries)
#plt.show()

# Write a program that makes a list called ages that has, the same number random
#values as salaries, (range:21 to 65) . Make scatter plot of this data
minSalary = 20000
maxSalary = 80000
numberofEnteries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberofEnteries)
ages = np.random.randint(low = 21, high = 65, size = numberofEnteries)

#plt.scatter(ages, salaries)
#plt.show()

#Add a line to this plot that shows y= x2 in a different colour.
#We can add label label = "salaries "
plt.scatter(ages, salaries, label = "salaries")

#add x squared 
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints 

plt.plot(xpoints, ypoints, color = 'r', label = "x squared")
#plt.show()

plt.title("random plot")
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.legend()
plt.show()
plt.savefig('New-Plot.png')
