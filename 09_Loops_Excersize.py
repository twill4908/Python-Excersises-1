#loop excersize
#1)create a program that asks the user for 8 names of people and store them in a list.
#When all the names have been given, pick a random one and print it.

#2) Create a guess game with the names of the colors. At each round pick a random color form the lsit and let user try to guess it.
#When he does it, ask if he wants to play again. Keep playing until the user types"no"

import random

name_list = []
while len(name_list) <8:
    names = input("Please enter a name :")
    break
print("Great job, here's a random number from that list: ", random.randstr(name_list) )
