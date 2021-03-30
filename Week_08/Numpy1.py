import numpy as np 

minSalary = 20000
maxSalary = 800000
numberOfEnt = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEnt)

NewSal = salaries + 1000
print(NewSal)
print (salaries)

salariesMult = salaries * 1.05 
print(salariesMult)

newSalaries = salariesMult.astype(int)
print(newSalaries)

import numpy as np
import matplotlib.pyplot as plt

plt.hist(salaries)
plt.show()
