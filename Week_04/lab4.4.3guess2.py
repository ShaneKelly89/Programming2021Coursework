#This program will tell user if their guess is too high or too low after each guess 

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else: 
        print("too high")
    guess = int(input("Please guess again:"))


print("Well done! Yes the number was ", numberToGuess)
