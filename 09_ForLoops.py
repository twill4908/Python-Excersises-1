#Loops


people = []

while len(people) <1:
    person = input("Type the name of a person: ")
    people.append(person)
    
    print(people)

# ------------
import random

number = random.randint(0,10)
guess = int (input ( "I'm thinking about a number between one and ten. Can you guess the number? ") )

while True:
    if guess == number:
        break
    else:
        guess = int (input ( "No, please try again. ") )
print(" You guessed it. The number I thought about was ", number)
            
