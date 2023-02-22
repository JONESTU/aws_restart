#imports for the current program
import random

#print comments about the program to the end user
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#variable called number is assigned to a random number from 1-10
number = random.randint(1,10)
#track if the user guessed number
isGuessRight = False

#while loop to handle game logic
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        