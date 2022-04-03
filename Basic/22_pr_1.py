# Write a program to print the multiplication table of a given number using for loop.
a = int(input("Enter a number: "))
for i in range(1,11):
    print(a,"X",i," = ",i*a)
print("\n")   
for i in range(1,11):
    print(f"{a}X{i} = {a*i}")