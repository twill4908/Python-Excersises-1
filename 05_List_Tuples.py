# Tuples are simiar to lists they just cannot be modified, good for example like months which is not changable, there are only 12 months and will ever only be 12 months
# Cann merge tuples, and list... but cannot merge it with eachother
# To remove from list use pop(), for specific index use pop(2), pop(0), etc..
# To remove from list you can also use remove(' X ')
# To Add to list use append(' X ')
# If you want to add to a particular place use append[0, 'X']


#Create a program with a predefined list of people. Ask the user for his name, add it to the end of the list and print the updated list.

people_list = ['Regina', 'Elizabbeth', 'Ryan', 'Ian']

name = input('Hello please enter your name so we can add you to our list: ')

people_list.append(name)

print('Thank you, our recent updated list has users: ', people_list)
