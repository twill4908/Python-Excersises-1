#Requests and JSON
#Create a quizzing game. Make an HTTP request to Open Trvia API at each round of the game to get  a new question and present it to the user to answer. 
# At the end of eachround ask the user if he wants to play again. Keep playing forver until the user types quit.
# Dont forget to tell if the answer is correct or not at the end of each round   

import json
import requests 
import random
import html

url = "https://opentdb.com/api.php?amount=1"
endGame = ""


input(print("We will play a game where you answer random questions, press enter to continue"))

while endGame != "quit":
    r = requests.get(url)
    if ( r.status_code != 200):
        endGame = input("Sorry, there was a problem retrieveing the question, please press enter to try again or, 'quit' to end the game.")
    else:
        answer_number = 1
        data = json.loads(r.text)
        #get question via object
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answers = data['results'][0]['correct_answer']
        answers.append(correct_answers)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answers in answers:
            print(str(answer_number) + " - " + html.unescape(answers))
            answer_number += 1
            input("")
