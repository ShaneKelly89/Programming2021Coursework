#Making a pie plot of the unique occerence of values in an array. 
#Author Shane Kelly 

import numpy as np 
import matplotlib.pyplot as plt 

#make the array of occurence 
possibleCounties = ['Cavan', 'Galway', 'Leitrim', 'Sligo', 'Clare', ]

#pick 100 randomly from possible counties with the frequence set in p 
counties = np.random.choice(
    possibleCounties , 
    p=[0.1, 0.3, 0.2, 0.12, 0.28 ],
    size=(100)
)
#now need the number of occurences of each county 
#this requires a tuple of the unique values and how many times they appear 
unique, counts = np.unique(counties, return_counts=True)
#we can now put this into a pie plot 

plt.pie(counts, labels= unique)
plt.show()

#modift to make bar chart 
plt.bar(unique, counts)
plt.show()
