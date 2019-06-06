# Dice roller for DnD
# Created by fineterra - https://github.com/fineterra

import random

# Ask user for type and number of dice
print("Available dice: d4, d6, d8, d10, d12, d20, d100")
die_type = input("What die do you want to roll?")
die_no = int(input("How many dice? "))

# Roll dice
roll = 0

if die_type == "d4":
    while die_no > 0:
        die = random.randint(1, 4)
        roll += die
        die_no -= 1

elif die_type == "d6":
    while die_no > 0:
        die = random.randint(1, 6)
        roll += die
        die_no -= 1

elif die_type == "d8":
    while die_no > 0:
        die = random.randint(1, 8)
        roll += die
        die_no -= 1

elif die_type == "d10":
    while die_no > 0:
        die = random.randint(1, 10)
        roll += die
        die_no -= 1

elif die_type == "d12":
    while die_no > 0:
        die = random.randint(1, 12)
        roll += die
        die_no -= 1

elif die_type == "d20":
    while die_no > 0:
        die = random.randint(1, 20)
        roll += die
        die_no -= 1

elif die_type == "d100":
    while die_no > 0:
        die = random.randint(1, 100)
        roll += die
        die_no -= 1

else:
    print("That die is not available")
    exit()

# Print results
print("\nYou rolled a", roll)
