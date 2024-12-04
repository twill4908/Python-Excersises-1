# Conditions

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
        
