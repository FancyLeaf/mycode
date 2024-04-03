#!/usr/bin/python3
""" Alta3 - Python Course, Lab 75
    Instructor: Paul Lack, Student: Michael Carter
    This lab covers tracking the iss using
    api.open-notify.org/astros.json | Alta3 Research
    This particular script will also incorporate the challenges for this lab:
        1. Print the output in a specific fashion """

# notice we no longer need to import urllib.request or json
import requests
import datetime

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

# Current date/time
when = datetime.datetime.now()

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    ## display our Pythonic data
    print("\nSpacer Status as of", when)
    people = str(helmetson["number"])
    print(f"People in space: {people}")
    for spacey in helmetson["people"]:
        print(spacey["name"] + " on the " + spacey["craft"])

if __name__ == "__main__":
    main()
