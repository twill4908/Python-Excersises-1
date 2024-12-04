
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
