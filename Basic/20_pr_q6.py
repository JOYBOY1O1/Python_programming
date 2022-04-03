'''
Write a program to calculate the grade of a student from his marks from the following scheme:
90-100	Ex
80-90	A
70-80	B
60-70	C
50-60	D
<50	    F       '''

a = int(input("Enter your marks: "))

if(90 <= a <= 100):
    grade = "Ex"

elif(80 <= a <= 90):
    grade = "A"

elif(70 <= a <= 80):
    grade = "B"

elif(60 <= a <= 70):
    grade = "C"

elif(50 <= a <= 60):
    grade = "D"

elif(a <=  50):
    grade = "F"
else:
    grade = "Fail"

print("Your grade is " + grade)
