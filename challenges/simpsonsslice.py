#!/usr/bin/env python3
""" Challenge 27 from Python course | Author: Michael Carter
    This is a challenge program to test our knowledge of slicing values 
    from "nested" lists and variables"""

# Variables are here!
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

lines = "*"*50
chall_word_1 = challenge[2][1]
chall_word_2 = challenge[2][0]
chall_word_3 = challenge[3]
trichar_1 = trial[2]["goggles"]
trichar_2 = trial[2]["eyes"]
trichar_3 = trial[-1]
nichar_1 = nightmare[0]["user"]["name"]["first"]
nichar_2 = nightmare[0]["kumquat"]
nichar_3 = nightmare[0]["d"]

# Functions are going in this area
def all_strings():
    print(f"My {chall_word_1}! The {chall_word_2} do {chall_word_3}!")
    print(f"My {trichar_1}! The {trichar_2} do {trichar_3}!")
    print(f"My {nichar_1}! The {nichar_2} do {nichar_3}!")

def main():
    all_strings()

if __name__ == "__main__":
    main()
