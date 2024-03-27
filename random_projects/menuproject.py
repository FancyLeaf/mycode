#!/usr/bin/env python3
""" Keystone Learning | Author: Michael Carter
    This is the menu prject we're practicing in class. Should consist of a menu, 
    and 2-3 options and further prompts if possible. """

# Variables placed here
title = "Danger Zone"
lines = "*"*50

option_1 = "1. Pass through the gateway."
option_2 = "2. Surveil your surroundings. "
option_3 = "3. Retreat from this place. "
option_4 = "4. Give up. "

# Definitions placed here
def show_menu():
    print(f"{lines}")
    print(f"You have approached the gateway to the {title}...")
    print(f"How should you proceed? ")
    menu_options()
    print(f"{lines}")

def menu_options():
    print(f"{option_1}\n{option_2}\n{option_3}\n{option_4}")

# Main functions will be placed here
def main():
    show_menu()

if __name__ == "__main__":
    main()
