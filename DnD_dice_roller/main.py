"""Dice roller for DnD"""
# by fineterra - https://github.com/fineterra
# a simple dice roller for DnD

import random

# create variables used by the functions
type = None
quantity = 0
modifier = 0
roll = 0


def user_input():
    """Determine which dice to use, how many, and if to use a modifier."""
    global type
    global quantity
    global modifier
    print("\nThe available dice are: 4, 6, 8, 10, 20, 100")
    valid_type = False
    valid_quantity = False
    while valid_type is False:
        type = int(input("\nWhat die do you want to roll? "))
        if type in {4, 6, 8, 10, 12, 20, 100}:
            valid_type = True
        else:
            print("That is not a valid die.")
    while valid_quantity is False:
        quantity = int(input("How many dice? "))
        if quantity > 0:
            valid_quantity = True
        else:
            print("That is not a valid quantity")
    modifier = int(input("What is the modifier? "))
    print()
    return type, quantity, modifier


def roll_dice(type, quantity, modifier):
    """Roll the dice and add a modifier if requested."""
    global roll

    # print every single roll result
    print("You rolled:")
    while quantity > 0:
        die = random.randint(1, type)
        roll += die
        quantity -= 1
        print(die)
    # add the modifier to the roll
    roll += modifier
    print("Added modifier:", modifier)

    return roll


def main():
    """Main program."""
    print("""
         -------------------------------
        |                               |
        |   Welcome to DnD Dice roller. |
        |                               |
         -------------------------------
    """)
    user_input()
    roll_dice(type, quantity, modifier)
    print("The total result is", roll)


# start the program
main()
input("\n\nPress the enter key to quit.")
