# Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))

if(s1<33 or s2<33 or s3<33):
    print("Fail")
elif((s1+s2+s3)/3 < 40):
    print("Fail")
else:
    print("Pass")