# Dice roller for DnD
# Created by fineterra - https://github.com/fineterra
import random

# Ask user for type and number of dice
print("\nAvailable dice: d4, d6, d8, d10, d12, d20, d100")
die_type = input("\nWhat die do you want to roll? ")
die_no = int(input("How many dice? "))
die_mod = int(input("What's the modifier? "))
print()

# Roll dice
roll = 0

if die_type == "d4":
    while die_no > 0:
        die = random.randint(1, 4)
        print("You rolled a", die)
        roll += die
        die_no -= 1

elif die_type == "d6":
    while die_no > 0:
        die = random.randint(1, 6)
        print("You rolled a", die)
        roll += die
        die_no -= 1

elif die_type == "d8":
    while die_no > 0:
        die = random.randint(1, 8)
        print("You rolled a", die)
        roll += die
        die_no -= 1

elif die_type == "d10":
    while die_no > 0:
        die = random.randint(1, 10)
        print("You rolled a", die)
        roll += die
        die_no -= 1

elif die_type == "d12":
    while die_no > 0:
        die = random.randint(1, 12)
        print("You rolled a", die)
        roll += die
        die_no -= 1

elif die_type == "d20":
    while die_no > 0:
        die = random.randint(1, 20)
        print("You rolled a", die)
        roll += die
        die_no -= 1

elif die_type == "d100":
    while die_no > 0:
        die = random.randint(1, 100)
        print("You rolled a", die)
        roll += die
        die_no -= 1

else:
    print("That die is not available")
    exit()

roll += die_mod

# Print results
print("\nThe total result is", roll)
