#loop excersize
#1)create a program that asks the user for 8 names of people and store them in a list.
#When all the names have been given, pick a random one and print it.

#2) Create a guess game with the names of the colors. At each round pick a random color form the list and let user try to guess it.
#When he does it, ask if he wants to play again. Keep playing until the user types"no"

import random

names = input("Please enter a name :")

name_list = [names]

while len(name_list) <8:
    break
print("Great job, here's the random name from that list: ", random.choice(name_list) )


print("---------------------------------------")

color = ["Pink", "Black", "Grey", "Red", "Blue", "Orange", "White", "Brown","Yellow", "Green", "Purple", "Maroon", "Turquoise", "Cyan", "Navy"]

rand_names = random.choice(color)

user_input = input("Lets play a game of guessing the correct color. Please input a color :")

while:
    if(rand_names != user_input):
    decision = input("Wrong color, do you want to play again: ")
    if(decision == "No", or, "no")
    break
    else:
    continue
else:
    print("Congrats, you guess the correct color of ", user_input)
