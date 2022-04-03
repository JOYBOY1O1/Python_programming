# Write a program to find whether a given username contains less than 10 characters or not.
a = input("Enter your username: ")
b = len(a)

if(b>10):
    print("username contains more than 10 characters")
else:
    print("username contains less than 10 characters")
print("Length of username: ",b)