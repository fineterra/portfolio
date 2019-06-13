# RPG Character Creator
# Give the user a pool of 30 points to spend on attributes
# Created by fineterra - https://github.com/fineterra


# create character
character = input("What's the name of your character? ")

# establish initial attributes and available points
points = 30
attributes = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}

# menu
choice = None

while choice != "0":
    addstat_choice = None
    remstat_choice = None
    print()
    print(character, "'s stats:", sep="")
    print(
        """
0 - Quit
1 - Check current stats
2 - Increase stats
3 - Decrease stats
        """
        )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Goodbye.")

    # print the current attributes and assigned points
    elif choice == "1":
        for k, v in attributes.items():
            print(k, ":", v)
        print("You have", points, "points left.")

    # increase the value of the stats
    elif choice == "2":
        if points < 1:
            print("You have no points left, try to decrease other stats.")
        else:
            while addstat_choice != "0":
                print(
                    """
What stat do you want to increase?
0 - Go back to previous menu
1 - Strength
2 - Health
3 - Wisdom
4 - Dexterity
                    """
                    )
                addstat_choice = input("Choice: ")
                print()
                if addstat_choice == "0":
                    print()
                elif addstat_choice == "1":
                    add_points = int(input(
                        "How many points would you like to add? "
                    ))
                    if add_points <= points:
                        attributes["Strength"] += add_points
                        points -= add_points
                        print("Done. Now Strength has", attributes["Strength"], "points.")
                        print("You have", points, "points left.")
                    else:
                        print("You don't have enough points available.")
                elif addstat_choice == "2":
                    add_points = int(input(
                        "How many points would you like to add? "
                    ))
                    if add_points <= points:
                        attributes["Health"] += add_points
                        points -= add_points
                        print("Done. Now Health has", attributes["Health"], "points.")
                        print("You have", points, "points left.")
                    else:
                        print("You don't have enough points available.")
                elif addstat_choice == "3":
                    add_points = int(input(
                        "How many points would you like to add? "
                    ))
                    if add_points <= points:
                        attributes["Wisdom"] += add_points
                        points -= add_points
                        print("Done. Now Wisdom has", attributes["Wisdom"], "points.")
                        print("You have", points, "points left.")
                    else:
                        print("You don't have enough points available.")
                elif addstat_choice == "4":
                    add_points = int(input(
                        "How many points would you like to add? "
                    ))
                    if add_points <= points:
                        attributes["Dexterity"] += add_points
                        points -= add_points
                        print("Done. Now Dexterity has", attributes["Dexterity"], "points.")
                        print("You have", points, "points left.")
                    else:
                        print("You don't have enough points available.")
                else:
                    print("That is not a valid choice.")

    # decrease the value of the stats
    elif choice == "3":
        if points >= 30:
            print("There's no stat to decrease.")
        else:
            while remstat_choice != "0":
                print(
                    """
What stat do you want to decrease?
0 - Go back to previous menu
1 - Strength
2 - Health
3 - Wisdom
4 - Dexterity
                    """
                    )
                remstat_choice = input("Choice: ")
                print()
                if remstat_choice == "0":
                    print()
                elif remstat_choice == "1":
                    rem_points = int(input(
                        "How many points would you like to remove? "
                    ))
                    if rem_points <= attributes["Strength"]:
                        attributes["Strength"] -= rem_points
                        points += rem_points
                        print("Done. Now Strength has", attributes["Strength"], "points.")
                        print("You have", points, "points left.")
                    else:
                        print("You don't have enough points left in Strength.")
                elif remstat_choice == "2":
                    rem_points = int(input(
                        "How many points would you like to remove? "
                    ))
                    if rem_points <= attributes["Health"]:
                        attributes["Health"] -= rem_points
                        points += rem_points
                        print("Done. Now Health has", attributes["Health"], "points.")
                        print("You have", points, "points left.")
                    else:
                        print("You don't have enough points left in Health.")
                elif remstat_choice == "3":
                    rem_points = int(input(
                        "How many points would you like to remove? "
                    ))
                    if rem_points <= attributes["Wisdom"]:
                        attributes["Wisdom"] -= rem_points
                        points += rem_points
                        print("Done. Now Wisdom has", attributes["Wisdom"], "points.")
                        print("You have", points, "points left.")
                    else:
                        print("You don't have enough points left in Wisdom.")
                elif remstat_choice == "4":
                    rem_points = int(input(
                        "How many points would you like to remove? "
                    ))
                    if rem_points <= attributes["Dexterity"]:
                        attributes["Dexterity"] -= rem_points
                        points += rem_points
                        print("Done. Now Dexterity has", attributes["Dexterity"], "points.")
                        print("You have", points, "points left.")
                    else:
                        print("You don't have enough points left in Dexterity.")
                else:
                    print("That is not a valid choice.")
    else:
        print("That is not a valid choice.")

input("\nPress enter to quit.")
