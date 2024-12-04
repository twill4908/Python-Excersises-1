#Excercise: Time & Pyplot

#Create a rogram to help the user type faster. Give them a word and ask them to type it five times
#Check how many seconds it took them to type the word at each round.

#At the end, tell the user how many mistakes were made and show a chart with the typing speed revolution during the 5 rounds.

#python3 -m pip install matplotlib

#import matplotlib.plot as plt
import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("This is a program to make you type faster, Type the word programming as fast as you can")

input("Press enter to continue.")


while len(times) < 5:
    start = t.time()
    word = input("Type te word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if(word.lower() != "programming"):
        mistakes += 1

print( "You made " + str(mistakes) + "mistakes")
print("Now lets see your eveolution")
t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x,legend)
plt.ylabel("Time in second")
plt.xlabel("Attempts")

plt.show()
