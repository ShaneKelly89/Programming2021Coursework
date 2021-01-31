#Bmi.py
#This program will be used to calculate a person's bmi
#Author Shane Kelly
weight = int(input("Enter weight here\n"))
height = float(input("Enter Height here\n"))
bmi = weight / (height * height)
print ("bmi is {}".format(bmi))

#Enter weight here first result below (changes made to Height (1.8))
#65
#Enter Height here
#180
#bmi is 0.002006172839506173

#Trial and error found height is expected to be in meters for this formula 
#to work. In line 6, we could input height to be divided by 100 (convert to cm
