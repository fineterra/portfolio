# Computer Guessing Game
# by fineterra - https://github.com/fineterra/
# The computer guesses the number chosen by the player

import random

print("\t\tWelcome to the 'Computer Guessing Name'.")

# Ask for the number and verify it's valid
try:
    number = int(input("Pick a random number between 1 and 100, "
                       "and the computer will guess it for you: "))
    pass
except Exception as e:
    print("It's not a number.")
    quit()

while number < 1 or number > 100:
    print("It's not a valid number.")
    try:
        number = int(input("Pick a random number between 1 and 100, "
                           "and the computer will guess it for you: "))
        pass
    except Exception as e:
        print("It's not a number.")
        quit()

# the computer guesses the number
tries = 1
guess = random.randint(1, 100)
while guess != number:
    if guess > number:
        guess = random.randint(1, guess)
        tries += 1
    elif guess < number:
        guess = random.randint(guess, 100)
        tries += 1

print("The computer guessed that the number is", guess)
print("It took", tries, "tries.")
input("\n\nPress Enter to quit.")
