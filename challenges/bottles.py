#!/usr/bin/env python3
""" In this challenge we'll be printing the "99 bottles of beer" song.
    For extra credits, we should do the following:
    1. Include input that allws the user to choose the amount of beers.
    2. Don't allow the user to enter a vlaue > 100. """

# Here we go with imports. I just like to add little delays.
import time

# Need to define our variables since we plan to use a 'while' loop
## Nevermind, reformatted to include the variable within 'main()'


# Let's place this all in a 'main()' function
def main():
    while True:
        bottles = input("How many bottles would we put on the wall? (1-100) ")
        if not bottles.isdigit():
            print("Okay funny guy, now enter an actual number!")
            continue
        bottles = int(bottles)
        if bottles > 100:
            print("That's far too many bottles! Choose less.")
            continue
        if bottles < 0:
            print("Okay, no more bottles. Goodbye!")
            break
        while bottles > 1:
            otw = f"{bottles} bottles of beer on the wall!"
            bob = f"{bottles} bottles of beer!"
            ytd = "You take one down, pass it around!"
            print(f"{otw}")
            time.sleep(0.5)
            print(f"{otw} {bob} {ytd}\n")
            bottles -= 1
            time.sleep(0.5)
        if bottles == 1:
            print(f"This is the last bottle of beer!")
            time.sleep(0.5)
            ootw = f"{bottles} bottle of beer on the wall!"
            last = f"{bottles} bottle of beer!" 
            lytd = "You take it down, pass it around!"
            print(f"{ootw}")
            time.sleep(0.5)
            print(f"{last}")
            time.sleep(0.5)
            print(f"{lytd}")
            time.sleep(0.5)
            print("No more bottles of beer on the wall! We are all out of beer!")        
        break


# Obligatory inclusion below
if __name__ == "__main__":
    main()
