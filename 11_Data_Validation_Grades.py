# Data Validation

data_valid = False

while data_valid == False:

    grade1 = float( input("Type the grade of the first test: ") )
    if grade1 < 0 or grade1 > 10:
        print("Grade should between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:

    total_classes = float( input("Type the total number of classes: ") )
    if total_classes <= 0:
        print("Classes should be greater than zero")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:

    absences = float( input("Type the amount of times student was absent: ") )
    if absences < 0 or absences > total_classes:
        print("The absences should be between 0 and the total classes")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:

    grade2 = float( input("Tpe the grade of the first test: ") )
    if grade2 < 0 or grade2 > 10:
        print("Grade should between 0 and 10")
        continue
    else:
        data_valid = True
    
    

grade1 = float( input("Type of grade for 1st test: ") )
grade2 = float( input("Type of grade for 2nd test: ") )
absences = int( input( " Type the number of absences: ") )
total_classes = int( input("Type the total # of classes: ") )

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade,2))
print( "Attendence rate: ", str(round((attendance * 100),2)) + '%')

if (avg_grade >= 6):
    if(attendance >= 0.8):
        print("This student has passed.")
    else:
        print("The student has failed due to the attendence rate being lower than 80%.")
elif (avg_grade >= 6):
    print("The student has failed dut to grade loweer the 60%")
else:
        print("The student has failed due to average grade below 60% and attendance rate below 80%")
        




