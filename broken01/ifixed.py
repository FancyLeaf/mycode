#!/usr/bin/env python3
""" This is for challenge 38 of the Python course from Alta3 Research
    We are given a little simple calculation program to troubleshoot.
    The goal being to fix it."""

# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = " "
while (calc1 != "q" or calc1 != "Q"): # Just added the capital "Q" here
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    if calc1 == "q" or calc1 == "Q":
        break
    calc1 = float(calc1)
    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input()
    if calc2 == "q" or calc2 == "Q":
        break
    calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")
        continue
# 'tis all fixed now. I did a backwards thing by adding "Q" to the if statements instead of
if __name__ == "__main__":
    main()
