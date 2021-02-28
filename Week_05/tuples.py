#This is a tuple which stores the months of the year
#From this tuple I will create another tuple, containing just the summer months 
#Author Shane Kelly 

months = ("January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
)
summer = months[4:7]
for month in summer:
    print(month)
