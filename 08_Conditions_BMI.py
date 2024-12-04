#Create a program to calculate the BMI of a person. Ask the user for his height in meters and his weight in kg.
# BMI = Body Mass Index
#BMI = weight / (height * height) -----> for KG height in meters
#BMI = weight / (height * height) ---> for pounds height in inches, 12 inches = 1 foot
# Print BMI and classification
#Less than or equal to 18.5: Underweight
#Greater than 18.5 or less than or equal to 24.9: Normal weight
#Greater than 24.9 or less than equal to 29.9: Overweight
#Greater than or equa; to 30: Obseity
print("This program calculatesws your Body Mass Index")


height = float( input("Pllease enter your height in meters: ") )
weight = float( input("Please enter your weight in kg. ") )

BMI= weight / (height ** 2)
print("Your BMI is: ", round(BMI,2) )

#Less than or equal to 18.5: Underweight
if( BMI <= 18.5):
    print("You are underweught")
#Greater than 18.5 or less than or equal to 24.9: Normal weight
elif( BMI > 18.5 or BMI <= 24.9):
    print("You are within normal weight")
#Greater than 24.9 or less than equal to 29.9: Overweight
elif( BMI < 24.9 or BMI <= 29.9):
    print("You are overweught")
#Greater than or equal to 30: Obseity
else:
    print(" You are overweight")
