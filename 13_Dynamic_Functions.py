# Functions
# To make dynamic use arguments of value we want to be printed
# def = function
# in parehtesis is the argument

#def say_hello
#say_hello('Tiara')
#say_hello('Janet')
#say_hello('Kayla')

def say_hello(person):
    print("Hello " + person + ", how are you doing today? ")

#need all arguents to be passed in same order
def say_hello(person1, person2):
    print("Hello " + person1 + ", how are you doing today? " + person2 + " Needs your help")

say_hello("Toni", "Balogni")

#Faren height to celcius function

def far2cels(fahr):
    celsius = (5 * (fahr -32)) / 9
    return celsius

print("Celsius: ", round(far2cels(100), 2) )
print("Kelvin: ", round(far2cels(100) + 273.5), 2 )
