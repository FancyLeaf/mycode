#!/usr/bin/env python3
"""RZFeeser@alta3.com | Alta3 Research
   Using the CSV library to work with CSV data."""

# standard library import
import csv
import time

# Manual script here
def manual():
    outFile = open("admin.rc", "a")
    osAUTH = input("What is the OS_AUTH_URL? ")
    print("export OS_AUTH_URL=" + osAUTH, file=outFile)
    print("export OS_IDENTITY_API_VERSION=3", file=outFile)
    osPROJ = input("What is the OS_PROJECT_NAME? ")
    print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)
    osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
    print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)
    osUSER = input("What is the OS_USERNAME? ")
    print("export OS_USERNAME=" + osUSER, file=outFile)
    osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
    print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)
    osPASS = input("What is the OS_PASSWORD? ")
    print("export OS_PASSWORD=" + osPASS, file=outFile)
    outFile.close()

#Automatic script goes here
# open our csv data (we want to loop across this)
def auto():    
    with open("csv_users.txt", "r") as csvfile:
        # counter to create unique file names
        i = 0
        # loop across our open file line by line
        for row in csv.reader(csvfile):
            i = i + 1 # increase i by 1 (to create unique admin.rc file names)
            filename = f"admin.rc{i}" # this f string says "fill in the value of i"

            # open a file via "with". This file will autoclose when the indentations stop
            with open(filename, "w") as rcfile:
                # use the standard library print function to print our data
                # out to the open file open rcfile (open in write mode)
                print("export OS_AUTH_URL=" + row[0], file=rcfile)
                print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
                print("export OS_USERNAME=" + row[3], file=rcfile)
                print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
                print("export OS_PASSWORD=" + row[5], file=rcfile)
    print("admin.rc files created!")

    # all of the indentation ends, so all files are auto closed
    # display this to the screen when all of the looping is over

def main():
    while True:
        mode = input("How would you like to handle setup? (manual/auto)\n").lower()
        if mode == "manual":
            print("Manual setup selected, please answer the questions below:")
            manual()
            selection = input("Would you like to enter another? (yes/no)\n ").lower()
            if selection == "yes":
                continue
            elif selection == "no":
                break
            else:
                print("Please type yes or no")
                continue
        elif mode == "auto":
            print("Automatic setup selected, sit back and enjoy!")
            auto()
            break
        else:
            print("Please make a valid selection and try again")
            continue


if __name__ == "__main__":
    main()

