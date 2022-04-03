#Write a program to detect double spaces in a string

a = input("Enter a string: ")
#print(a.count("  "))
double_spaces = a.find("  ")
print("The index of double space is :",double_spaces)


#Replace the double spaces from problem 3 with single spaces.

print(a.replace("  "," "))