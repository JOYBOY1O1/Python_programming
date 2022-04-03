# Write a program to find the greatest of four numbers entered by the user.

n1 = int(input("1 Enter a number: "))
n2 = int(input("2 Enter a number: "))
n3 = int(input("3 Enter a number: "))
n4 = int(input("4 Enter a number: "))

if(n1>n2):
    f1 = n1
else:
    f1 = n2
    
if(n3>n4):
    f2 = n3
else:
    f2 = n4
if(f1>f2):
    print(str(f1) +" is Greater")
else:
    print(str(f2) +" is Greater")