# Booleans and Conditions
# Create a program  and store your age in a variaable. Then ask the user for his age and print whether:
# User is older than you
# User is younger than you
# You are both the same age

my_age = 27

user_age = int( input( "Please enter your age: ") )

if (my_age < user_age):
   print('User is older than me!')
elif (my_age == user_age):
       print('User and I are the same age!')
else:
    print('User is younger than me!')
