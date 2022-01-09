import random
from random import randint

# Initialize program
print("Welcome to the number guessing game!")
seed = input("Enter random seed: ")
random.seed(seed)
play = True

while play != "no":
    # Initialize starting numbers
    turns = 0
    guess = 0
    num = randint(1, 100)
    print()

    # Start round
    while guess != num:
        turns += 1
        guess = int(input("Please enter a guess: "))
        if guess > num:
            print("Lower" + "\n")
        elif guess < num:
            print("Higher" + "\n")
    
    print(("Congratulations. You guessed it!" + "\n" + "It took you %i guesses.\n") % (turns))
    play = input("Would you like to play again (yes/no)? ").lower()

# End program
print("Thank you. Goodbye.")