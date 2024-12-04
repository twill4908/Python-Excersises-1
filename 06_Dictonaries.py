# Data Dictoriaries
# Key: Value Pairs

# List = [], Tuple = (), Dictonary = {}

# ex: person = {"first_name": "John", "last_name": "Green", "birth_year": 1997, "COB": "United States"}

# person type is dictonary not list

# Key = 'first_name'    > John
# To delete everything person.clear()
# Can also use get command to find keys, person.get()


# Create a program with a predefinned dictonary, include name, gender, age, address, and phone.
# Ask the user what informattion he wants to know about the person (example: name), then print the value associated to that key or display a message in case the  key is not found.

person = {'name': 'Getonia Kapleck', 'gender': 'female', 'age': 34,
           'address' : '106 Smith St, New York, NY, 10001',
           'phone' : '347-876-3579'}

recieved = input('What information do you want to know about the user, specifically pertaining to name, gender, age, address, and phone? ')

#get(recieved)



print('The information associated with ,', recieved, ' is ',  person.get(recieved))

#OR USE Below Script (more efficient with handling errors

result = person.get(recieved, 'Sorry, we do not have such information avialble.')

print(result)
