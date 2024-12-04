# Create a program that asks the user for his forst name, his middle name and his last name.
#Then print Your 'initials are _____'

fname = input("Please enter your first name: ") 

mname = input("Please enter your fmiddle name: ") 

lname = input("Please enter your last name: ") 

print('Your initials are: ', fname[0] + ' ' + mname[0] + ' ' + lname[0])




# Lets say your company has a product w lot number: "037-00901-00027".
# 037 is the country code. 00901 is the product code. 00027 is the batch number.
# Create a program to print
# Country Code: ____
# Product Code: ____
# Batch Number: _____


print('Your company has a product with a lot number: "037-00901-00027"')

lot_num = '037-00901-00027'

print('Country Code :', lot_num[:3])

print('Product Code :', lot_num[4:9])

print('Batch Code :', lot_num[10:])
      
