# Tuples are simiar to lists they just cannot be modified, good for example like months which is not changable, there are only 12 months and will ever only be 12 months
# Cann merge tuples, and list... but cannot merge it with eachother
# To remove from list use pop(), for specific index use pop(2), pop(0), etc..
# To remove from list you can also use remove(' X ')
# To Add to list use append(' X ')
# If you want to add to a particular place use append[0, 'X']


# Create a program that asks the user for his birthday in the format DD-MM-YY. Then print 'You were born in [month]'

import datetime
import calendar

dob = input(' Please enter your date of birth in the format DD-MM-YYYY: ')

months = ('January' 'Febuary', 'March', 'April', 'May', ' June', 'July', 'Agust', 'September', 'October', 'November', 'December')

year = dob[5:]
month = dob[3:5]
day = dob[0:3]

this_month = int(month)

print(' You were born in ', months[this_month])

#print(' You were born in ', calendar.month_name[dob[3:5]])


