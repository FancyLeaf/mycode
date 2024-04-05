#!/usr/bin/env python3
""" Capstone Project - Dungeon Labyrinth
    Author - Michael Carter (Github: FancyLeaf)
    This is my Capstone Project for the TLG Learning Python Course 
    instructed by the awesome team at Alta3 Research. Thanks Paul! """
# Importing necessary methods and functions
import time # I can't seem to write anything interactive without adding a delay here and there
import random # If I can, I'd like to randomize bits of this program
import os # I have a sneaking suspicion that this will be needed in order to make save files

""" Objectives are going to go here, where they will be an ever-present reminder of how much more I need to do.
    1. Main menu
        1a. Should provide title, and a check for save-file
        1b. Should provide instructions for the game and prompt user to continue to menu
        1c. Should show menu options and allow user to return back to intro or exit game
    2. Movement system (dictionary-based map) - Highest priority right now
        2a. Should move the user through the dungeon
        2b. Should show only the available directions for each room
        2c. Minotaur should be bound by the same rules here
    3. Interactions with environment
        3a. Users should receive some sort of information for their room
        3b. Users should receive some sort of information about neighboring rooms (sounds, smells, etc.)
        3c. Wishlist Item - Special interactions (class-specific info/attacks, *new pathway creation*)
    4. Combat system (counter-based)
        4a. Basic combat (i.e. hit stuff and be hit by stuff, turn-based and not unfair)
        4b. Should provide a use for that inventory, right?
    5. Inventory system
        5a. Should be able to display current inventory when prompted
        5b. Should provide hints on anything useful in inventory depending on environ
    6. Class system
        6a. Should be able to choose between a few classes at least
        6b. Classes should have unique properties (attacks, HP, etc.)
    7. Save system
        7a. Should allow the user to save game at any point
        7b. Should create a save file with the user's character data, as well as that of the labyrinth
    8. Adventure Logs
        8a. Should be able to pull from save directory to give a brief overview of total adventure data
        8b. Notable accomplishments?? (Moved through 50 rooms, defeated 20 monsters, etc.)
    9. Minotaur
        9a. Does minotaur stuff
        9b. "Chases" the player
        9c. Creates new pathways (this will be limited, but I should be able to do a little logic check and dictionary addition)
    Almost too easy to even think about. """
        

# Our global variables and dictionaries will be here, to be referenced in the code below.
## Though, I'd like to just import them from a separate file to keep this as clean and simple as possible.
intro_1 = f"You awaken in front of the labyrinth."
intro_2 = f"You can control your movement in each section by typing the corresponding command displayed."
intro_3 = f"Be aware... You are not the only one that moves within... "
intro_options = ["yes", "no", "y", "n"]
menu_1 = f"1. Enter the Labyrinth. "
menu_2 = f"2. Observe the area. "
menu_3 = f"3. Open your pack. "
menu_4 = f"4. Flee (End run and exit game). "
menu_options = f"Please make your choice:\n{menu_1}\n{menu_2}\n{menu_3}\n{menu_4}\n"

# Any sub-functions I want will be entered in this space, if not imported from another file.


# Now the main course. The "Meat & Potatoes".
def main():
    while True:
        print(intro_1)
        time.sleep(1)
        print("This is where the save check should go!")
        time.sleep(1)
        print(intro_2)
        time.sleep(1)
        print(intro_3)
        intro_input = input("Are you ready to begin? (yes/no)\n").lower()
        if intro_input != ["yes", "no"]:
            print("Please make a valid selection. ")
            continue
        elif intro_input == "no":
            print("Likely a wise choice for one such as you... Be gone.")
            break
        time.sleep(1)



# Obligatory "play nice" bit below
if __name__ == "__main__":
    main()