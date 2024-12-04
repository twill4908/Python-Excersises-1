
user_kilo = float( input(" Please enter a number of Kilometers: ") )

# Given Information
# 1 Mile = 1.609344 kilometers (km)
# So that means when user enter 5 km, the calculations will take what user enter against what an actual mile is
miles = user_kilo / 1.609344

print(user_kilo, " kilometers converted to miles, is ", round(miles,4), "miles.")

       
