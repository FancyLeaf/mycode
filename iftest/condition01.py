#!/usr/bin/env python3
""" Lab 32 - Python Course | Directed by Rob Schneider ft: FancyLeaf (Author is RZFeeser@alta3.com).
    We're practicing if statements on this one, with an associated printout 
    when the user enters the correct response. """

# Where's the fun if we don't make it a bit more interesting, let's add imports
import time

# We'll start our main function now

def main():
    while True:
        hostname = input("What value should we set for hostname? ")
        if hostname.upper() == "MTG":
            print(f"Checking supplied response against database... ")
            time.sleep(1)
            print(f"The hostname provided matches expected config, confirming change, please standby... ")
            time.sleep(1)
            print(f"The hostname has been changed. Verifying change success... ")
            time.sleep(1)
            print(f"The hostname was found to be MTG. Change verified.")
            break
        else:
            print(f"Checking supplied response against database... ")
            time.sleep(2)
            print(f"The hostname provided does not match expected config.")
            print(f"Please verify desired hostname and try again.")
            continue # This will repeat the "while" loop until the user gets a correct answer
        # Telling the user we're done here
        print(f"Exiting the script")

if __name__ == "__main__":
    main()

