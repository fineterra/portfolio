"""Play a game of chance."""
# by fineterra - https://github.com/fineterra/
# The player can choose between four different games of chance, and bet on it.
# Inspired by a Codecademy project

import random
import os

money = 100

# Write your game of chance functions here


def welcome_screen():
    """Print a welcome screen."""
    print("""
         --------------------------------
        |                                |
        |   Welcome to Game of Chance.   |
        |                                |
         --------------------------------

    To play, select a game from the menu below,
    or look up the instructions for each game.

    """)
    menu()


def menu():
    """Print the menu."""
    # Display the menu
    print("""
    Press the number corresponding to your choice:
    1. How to play
    2. Check available money
    3. Flipping coin
    4. Cho-Han
    5. Cards
    6. Roulette
    7. Exit
    """)

    choice = input(" ")
    choice = int(choice)
    # Clear the window for ease of read
    os.system('cls' if os.name == 'nt' else 'clear')
    # Call the correct function based on user input
    if choice == 1:
        instructions()
    elif choice == 2:
        available_money()
    elif choice == 3:
        flipping_coin()
    elif choice == 4:
        cho_han()
    elif choice == 5:
        cards()
    elif choice == 6:
        roulette()
    elif choice == 7:
        print("")
    else:
        print(choice, "is not a valid choice.")


def instructions():
    """Print instructions for the various games."""
    # Display the menu
    print("""
    Which game would you like to hear an explanation of?
    1. Flipping coin
    2. Cho-Han
    3. Cards
    4. Roulette
    5. Go back
    """)
    choice = input(" ")
    choice = int(choice)

    # Keep asking an input to the user until they choose to go back to menu()
    while choice != 5:
        if choice == 1:
            print("""
            Select a side of the coin you would like to bet on.
            A coin will be flipped, and if you guessed correcly
            the side it lands on, you'll win and double your bet.
            """)
            choice = input(
                "Which game would you like to hear an explanation of? "
            )
            choice = int(choice)
        elif choice == 2:
            print("""
            Cho-Han is a traditional Japanese game.
            You roll two dice and try to guess if their sum is going
            to be odd or even. If you guessed correctly,
            you'll win and double your bet.
            """)
            choice = input(
                "Which game would you like to hear an explanation of? "
            )
            choice = int(choice)
        elif choice == 3:
            print("""
            Both you and the House draw a card. The higher card wins.
            If you win, you'll get five times your bet.
            It there is a tie, you will get back your bet.
            """)
            choice = input(
                "Which game would you like to hear an explanation of? "
            )
            choice = int(choice)
        elif choice == 4:
            print("""
            You can choose between odd, even, or a specific number
            between 0 and 36.
            If you guess correctly you win.
            If you bet on odd or even, you'll double your bet (1:1).
            If you bet on a specific number you'll win 35 times your bet (35:1).
            Careful though: a 0 doesn't count as even.
            """)
            choice = input(
                "Which game would you like to hear an explanation of? "
            )
            choice = int(choice)
        else:
            print("That is not a valid choice.")
            choice = input(
                "Which game would you like to hear an explanation of? "
            )
            choice = int(choice)

    input("\nPress ENTER to return to the main menu.")
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()


def available_money():
    """Print available money."""
    print("You have £" + str(money) + " available.")
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()


def bet_amount():
    """Ask for a bet and return it for other functions."""
    global money
    global bet
    valid_bet = False
    # Keep asking for an input until the input is valid
    while valid_bet is False:
        print("You have £" + str(money) + " available.")
        bet = input("How much would you like to bet? ")
        bet = int(bet)
        if 0 < bet < money:
            valid_bet = True
            return bet
        else:
            print(bet, "it's not a valid amount.")


def flipping_coin():
    """Ask what to bet on, flip a coin, and give result to player."""
    global bet
    global money

    bet_amount()

    # Ask user what to bet on
    print("""
    Choose on what to bet:
    1. Heads
    2. Tails
    """)
    choice = input("Enter your choice: ")
    if choice == "1" or choice.upper() == "HEADS":
        choice = "heads"
    elif choice == "2" or choice.upper() == "TAILS":
        choice = "tails"
    else:
        print("That choice is not supported.")

    # Flip the coin
    coin = random.choice(["heads", "tails"])

    # Print if won or lost and by how much
    if choice.upper() == coin:
        winnings = bet * 2
        money = money + winnings
        print("You won! The result is " + coin + ". You won £" +
              str(winnings) + ".")
        print("You now have £" + str(money) + ".")
    else:
        money = money - bet
        print("Oh no, you lost. The result is " + coin + ". You lost £"
              + str(bet) + ".")
        print("You now have £" + str(money) + ".")

    input("\nPress ENTER to return to the main menu.")
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    return money


def cho_han():
    """Ask what to bet on, throw 2 dice, and give result to player."""
    global money
    global bet
    bet_amount()
    # Ask user what to bet on
    print("""
    Choose on what to bet:
    1. Odd
    2. Even
    """)

    choice = input("Enter your choice: ")
    if choice == "1" or choice.upper() == "ODD":
        choice = "odd"
    elif choice == "2" or choice.upper() == "EVEN":
        choice = "even"
    else:
        print("That choice is not supported.")

    # Throw dice and determine if odd or even
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice = die1 + die2
    result = dice % 2
    print("You rolled a " + str(die1) + " and a " + str(die2) +
          ", for a total of " + str(dice) + ".")

    if result == 0:
        result = "even"
    else:
        result = "odd"

    # Print if won or lost and by how much
    if result == choice:
        winnings = bet * 2
        money = money + winnings
        print("You won! The total is " + result + ". You won £" +
              str(winnings) + ".")
        print("You now have £" + str(money) + ".")
    else:
        money = money - bet
        print("Oh no, you lost. The total is " + result.title() +
              ". You lost £" + str(bet) + ".")
        print("You now have £" + str(money) + ".")

    input("\nPress ENTER to return to the main menu.")
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    return money


def cards():
    """Ask what to bet on, draw two cards, and print the result."""
    global money
    global bet
    bet_amount()
    input("\nPress ENTER to draw a card.")

    # The player draw a card
    player_card = random.randint(1, 13)
    if player_card == 1:
        print("Your card is an Ace.")
    elif 1 < player_card < 11:
        print("Your card is a " + str(player_card) + ".")
    elif player_card == 11:
        print("Your card is a Jack.")
    elif player_card == 12:
        print("Your card is a Queen.")
    elif player_card == 13:
        print("Your card is a King.")

    # The House draw a card
    pc_card = random.randint(1, 13)
    if pc_card == 1:
        print("The House's card is an Ace.")
    elif 1 < pc_card < 11:
        print("The House's card is a " + str(pc_card) + ".")
    elif pc_card == 11:
        print("The House's card is a Jack.")
    elif pc_card == 12:
        print("The House's card is a Queen.")
    elif pc_card == 13:
        print("The House's card is a King.")

    # Print if won or lost and by how much, or if it's a tie
    if player_card > pc_card:
        winnings = bet * 5
        money = money + winnings
        print("You won! Your card was higher. You won £" +
              str(winnings) + ".")
        print("You now have £" + str(money) + ".")
    elif player_card < pc_card:
        money = money - bet
        print("Oh no, you lost. Your card was lower. You lost £"
              + str(bet) + ".")
        print("You now have £" + str(money) + ".")
    else:
        print("It's a tie! You get your money back.")
        print("You still have £" + str(money) + ".")

    input("\nPress ENTER to return to the main menu.")
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    return money


def roulette():
    """Ask what to bet on, generate a number, and print the result."""
    global money
    global bet
    bet_amount()
    # Ask user what to bet on
    print("""
    Choose on what to bet:
    1. Odd
    2. Even
    3. Number
    """)

    # Keep asking until the choice is valid
    valid_choice = False
    while valid_choice is False:
        choice = input("Enter your choice: ")
        if choice == "1" or choice.upper() == "ODD":
            choice = "odd"
            valid_choice = True
        elif choice == "2" or choice.upper() == "EVEN":
            choice = "even"
            valid_choice = True
        elif choice == "3" or choice.upper() == "NUMBER":
            choice = "number"
            num = input("Enter the number you would like to bet on: ")
            num = int(num)
            if 0 <= num <= 36:
                valid_choice = True
            else:
                print("That choice is not supported.")
        else:
            print("That choice is not supported.")

    number = random.randint(0, 36)

    # Print if won or lost and by how much
    if choice == "even" and number % 2 == 0 and number != 0:
        winnings = bet
        money = money + winnings
        print("You won! The result is " + str(number) + ". You won £" +
              str(winnings) + ".")
        print("You now have £" + str(money) + ".")
    elif choice == "odd" and number % 2 == 1:
        winnings = bet
        money = money + winnings
        print("You won! The result is " + str(number) + ". You won £" +
              str(winnings) + ".")
        print("You now have £" + str(money) + ".")
    elif choice == "number" and num == number:
        winnings = bet * 35
        money = money + winnings
        print("You won! The result is " + str(number) + ". You won £" +
              str(winnings) + ".")
        print("You now have £" + str(money) + ".")
    else:
        money = money - bet
        print("Oh no, you lost. The result is " + str(number) + ". You lost £"
              + str(bet) + ".")
        print("You now have £" + str(money) + ".")

    input("\nPress ENTER to return to the main menu.")
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    return money


# Main program
welcome_screen()
