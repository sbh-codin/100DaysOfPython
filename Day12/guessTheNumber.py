import random

def randomGenerator():
    number = random.choice(numberList)
    return number
def guessChecker(guess,level):
    """"To check if user guessed the number right"""
    lives = 0
    while lives == 0:
        if level == "e":
            lives = 9
        elif level == "h":
            lives = 4
        else:
            level = input("Enter only 'e' or 'h'")
    #generating a random number
    randomNumber = randomGenerator()
    while(lives > 0):
        if(guess > randomNumber):
            guess = int(input("Too high!! Please guess again. "))
        elif guess < randomNumber:
            guess = int(input("Too Low!! Please guess again. "))
        else:
            print(f"You guessed it correct. The number is {guess}")
            exit()
        lives -= 1

#1. random number list
numberList = list(range(1,101))
#2. Get all the user inputs
level = input(" What game level do you want to play? press 'e' for easy and 'h' for hard ")
# Get the user input
guessedNumber = int(input("Guess a number between 1 and 100. "))

#3. Calling the main calculator
guessChecker(guessedNumber,level)
  