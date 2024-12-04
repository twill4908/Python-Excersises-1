# Create a program to calculate the area and cicumfrence of a circfle. Ask for radius
#  Area = 3.14 x r^2
# Circumfrence = 2 * 3.14 * r
# r = raidus

import math

r = float( input('Please enter a radius: ') )

area = math.pi * math.pow(r,2) 
circum = 2 * math.pi * r

print('Thea area of ', r ,' is ', round(area,2), ' and the circumfrence of ', r ,' is ', round(circum,2))
