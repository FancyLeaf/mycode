""" This bit here is just the classes for both the Minotaur and the Player
    separated from the main script to keep it a bit cleaner. """
import random

# Player class, to be expanded upon once I get to combat or other fun little items
class Player:
    def __init__(self, name, start_position, dungeon_map):
        self.name = name
        self.position = start_position
        self.dungeon_map = dungeon_map
        self.inventory = {
            "gold": 0,
            "potions": 0,
            "weapons": [],
            "scrolls": [],
        } # Not any use for an inventory right now, but there will be in future versions
        self.distance_travelled = 0  # Setting the distance travelled, so I can log it later
        self.health = 3  # Keeping it simple with just 3 health

    def move(self, direction): # Moving!
        if direction in self.dungeon_map[self.position]:
            destination = self.dungeon_map[self.position][direction]
            if destination not in ["Wall", "Outwall"]: # This phrasing stops walls from appearing as options
                self.position = destination
                print("You move", direction)
                self.distance_travelled += 1
                return True
            else:
                print("It appears there's a wall blocking your path.")
        else:
            print("That is not a valid move, please try again.")
        return False

    def decrease_health(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

# Our antagonist in this labyrinth. For now, just a game of tag. 
        """ This keeps track of how many times the player is caught by the minotaur.
        Currently, it's being used to keep track of when the game ends, but it 
        could be added later to the adventure log as a fun statistic. """

class Minotaur:
    def __init__(self, start_position, dungeon_map):
        self.position = start_position
        self.dungeon_map = dungeon_map
        self.catch_counter = 0
        self.moved_this_turn = False  # Flag to track whether the Minotaur has moved during the current turn

    def move_towards_player(self, player_position):
        if self.moved_this_turn:  # Check if the Minotaur has already moved during this turn
            return

        # Get adjacent rooms
        adjacent_rooms = [room for direction, room in self.dungeon_map[self.position].items()
                          if room not in ["Wall", "Outwall", "Entrance", "Exit"]]
        
        # If the player is adjacent, move towards the player
        if player_position in adjacent_rooms:
            self.position = player_position
        else:
            # Choose a random adjacent room
            next_room = random.choice(adjacent_rooms)
            self.position = next_room

        self.moved_this_turn = True  # Mark that the Minotaur has moved during this turn


    # Did the minotaur catch the player?
    def check_player_collision(self, player_position):
        return self.position == player_position

    def increase_catch_counter(self):
        self.catch_counter += 1

    # Game over, man. Uses the catch counter to end the game
    def check_game_over(self):
        return self.catch_counter >= 3

    # Cheating minotaur was keeping the player locked in its grip, so, this teleports it away after contact
    def teleport_randomly(self):
        valid_positions = [position for position in self.dungeon_map.keys() if position not in ["Wall", "Outwall", "Entrance", "Exit"]]
        self.position = random.choice(valid_positions)

