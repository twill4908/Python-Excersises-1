#Apply the try and except statements to the students grades program ans keep it from crashing.

# Data Validation

#incorrect version with error

# number = float( input( "Type a number: ) )

print("----------------------------------------------------------- GRADE ONE -----------------------------------------------------------")


data_valid = False

while data_valid == False:

    grade1 = input("Type the grade of the first test: ")

    try:
        grade1 =float(grade1)
        
    except:
        print("Invalid grade, non comma numbers are accepted")
        continue

    if grade1 < 0 or grade1 > 10:
        print("Grade should between 0 and 10")
        continue
    else:
        data_valid = True

print("----------------------------------------------------------- GRADE TWO -----------------------------------------------------------")


data_valid = False

while data_valid == False:

    grade2 = input("Type the grade of the second test: ")

    try:
        grade2 =float(grade2)
        
    except:
        print("Invalid grade, non comma numbers are accepted")
        continue

    if grade2 < 0 or grade2 > 10:
        print("Grade should between 0 and 10")
        continue
    else:
        data_valid = True

print("----------------------------------------------------------- CLASSES -----------------------------------------------------------")

data_valid = False

while data_valid == False:

    total_classes = input("Type the amount of classes for this subject this semester: ") 
    try:
        total_classes =int(total_classes)

    except:
         print("Invalid grade, non comma numbers are accepted")
         continue
    
    if total_classes <= 0:
        print("Classes should be greater than zero")
        continue

    else:
        data_valid = True
    
print("----------------------------------------------------------- ABSENCES -----------------------------------------------------------")


data_valid = False

while data_valid == False:

    absences = input("Type the amount of times student was absent: ")

    try:
        absences =int(absences)
        
    except:
        print("Invalid grade, non comma numbers are accepted")
        continue

    if absences < 0 or absences > total_classes:
        print("The absences should be between 0 and the total classes")
        continue
    
    else:
        data_valid = True




print("----------------------------------------------------------- RESULTS -----------------------------------------------------------")


avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade,2))
print( "Attendence rate: ", str(round((attendance * 100),2)) + '%')

if ((avg_grade >= 6) and (attendance >= 0.8)):
    print("This student has passed.")
elif ((avg_grade < 6) and (attendance < 0.8)):
    print("The student has failed due to the attendence rate being lower than 80%.")
elif (avg_grade >= 6):
    print("The student has failed dut to grade loweer the 60%")
else:
    print("The student has failed due to average grade below 60% and attendance rate below 80%")
        




