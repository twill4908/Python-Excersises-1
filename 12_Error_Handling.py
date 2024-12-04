#Error Handling

# Use Try and accept statement so program wn't crash

#incorrect version with error

# number = float( input( "Type a number: ) )

number = input( "Type a number: ")
try:
    number = float(number)
    print("The nuumber is: ",number )
except:
              print("Invalid number")
