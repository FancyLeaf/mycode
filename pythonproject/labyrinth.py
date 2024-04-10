#!/usr/bin/env python3
""" Capstone Project - Dungeon Labyrinth
    Author - Michael Carter (Github: FancyLeaf)
    This is my Capstone Project for the TLG Learning Python Course 
    instructed by the awesome team at Alta3 Research. Thanks Paul! """
# Importing necessary methods and functions
import time # I can't seem to write anything interactive without adding a delay here and there
import random # If I can, I'd like to randomize bits of this program
# Not in use import os # I have a sneaking suspicion that this will be needed in order to make save files
import math # This will be used to calculate distance between minotaur and player, not currently in use
import labmap # Here's our labyrinth (10x10 right now)
import labyrinthclasses # Our "class" definitions for the player and the Minotaur

""" Objectives are going to go here, where they will be an ever-present reminder.
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
        8b. Notable accomplishments?? (Moved through 51 rooms, defeated 20 monsters, etc.)
    9. Minotaur
        9a. Does minotaur stuff
        9b. "Chases" the player
        9c. Creates new pathways (this will be limited, but I should be able to do a little logic check and dictionary addition)
    Almost too easy to even think about. """
        

# Our global variables and dictionaries will be here, to be referenced in the code below.
## Though, I'd like to just import them from a separate file to keep this as clean and simple as possible.
intro_1 = f"You awaken in front of the labyrinth."
intro_2 = f"You can control your movement in each room by typing the corresponding command displayed."
intro_3 = f"Be aware... You are not the only one that moves within... "

# Here's how we tie-in our map
dungeon_map = labmap.sectors

# We have to set the initial player position, in our case that's A6
player_position = "A6"

# Any sub-functions I want will be entered in this space, if not imported from another file.
def intro_ready():
    while True:
        print(intro_1)
        time.sleep(1)
        print(intro_2)
        time.sleep(1)
        print(intro_3)
        time.sleep(1)
        response = input("Are you ready to begin? (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            time.sleep(1)
            print("We'll find out soon enough... ")
            return True
        elif response in ["no", "n"]:
            time.sleep(1)
            print("Likely a wise choice for one such as you... Be gone.")
            return False
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

# Let's see which room the player is in
def display_room_info(room):
    print("You are in room", room)
    time.sleep(1)
    print("Available moves: ")
    for direction, destination in dungeon_map[room].items():
        if destination not in ["Wall", "Outwall"]:
            print(f"{direction}: {destination}")

# Movement function goes here!
def move_player(direction):
    global player_position
    if direction in dungeon_map[player_position]: # Is this a valid choice?
        destination = dungeon_map[player_position][direction]
        if destination not in ["Wall", "Outwall"]:
            player_position = destination
            print("You move", direction)
        else:
            print("It appears there's a wall blocking your path.")
    else:
        print("That is not a valid move, please try again.")

# Now the main course. The "Meat & Potatoes".
def main():
    player_name = input("Enter your name: ")
    player = labyrinthclasses.Player(player_name, "A6", dungeon_map)
    minotaur = labyrinthclasses.Minotaur("B1", dungeon_map)

    while True:
        if intro_ready():
            break

    while True:
        minotaur.moved_this_turn = False
        display_room_info(player.position)
        user_input = input("Choose a direction, or type 'quit' to exit (North, South, East, West): ").strip().title()
        if user_input.lower() == "quit":
            print("Giving up already, are we?")
            time.sleep(1)
            print("Exiting program...")
            break
        moved = player.move(user_input)
        if moved:
            # Minotaur moves one step towards the player
            minotaur.move_towards_player(player.position)
            print(f"The Minotaur has entered room {minotaur.position}")
            if minotaur.check_player_collision(player.position):
                print("The Minotaur caught you!")
                player.decrease_health()
                print(f"Your health: {player.health}")
                if player.is_alive():
                    print("Seems the Minotaur isn't done with you just yet...")
                    minotaur.teleport_randomly()
                else:
                    print("The Minotaur has grown bored of this chase. Game over!")
                    time.sleep(1)
                    print(f"Distance travelled: {player.distance_travelled}")
                    break
            if minotaur.check_game_over():
                print("The Minotaur caught you three times! Game Over!")
                break


# Obligatory "play nice" bit below
if __name__ == "__main__":
    main()
