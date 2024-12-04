#loop excersize
#1)create a program that asks the user for 8 names of people and store them in a list.
#When all the names have been given, pick a random one and print it.

import random

name_list = []

for x in range(0,8):
    names = input("Please enter a name :")
    name_list.append(names)

index = random.randint(0,7)
rand_name = name_list[index]

    
print("Great job, here's a random name from that list: ", random.choice(name_list) )


print("---------------------------------------")

#2) Create a guess game with the names of the colors. At each round pick a random color form the list and let user try to guess it.
#When he does it, ask if he wants to play again. Keep playing until the user types"no"


colors = ["Pink", "Black", "Grey", "Red", "Blue", "Orange", "White", "Brown","Yellow", "Green", "Purple", "Maroon", "Turquoise", "Cyan", "Navy"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("Lets play a game of guessing the correct color. Please input a color :")

    while True:
        if(color == guess):
            break
        
        else:
            new_guess = input("Wrong color, Try again: ")

    print("Congrats, you guess the correct color of ", new_guess)

            
    play_again = input("Do you want to play again, type no to quit: ")
    
    if play_again.lower() == "no":
        break
            
print("This was fun, Thanks for playing:n ")
