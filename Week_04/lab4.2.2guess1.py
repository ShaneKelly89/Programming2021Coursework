#This is a porogram which prompts the use to guess a number
#It will continue to promt until the user gets the correct number 
#Author Shane Kelly 

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))


print ("Well done! Yes the number was ",numberToGuess)


