'''
A spam comment is defined as a text containing the following keywords:
“make a lot of money”, “buy now”, “subscribe this”, “click this”. 
Write a program to detect these spams.
'''
a = input("Enter a string: ")
spam = False

if("make a lot of money" in a):
    spam = True
elif("buy now" in a):
    spam = True
elif("click this" in a):
    spam = True
elif("subscribe this" in a):
    spam = True
else:
    spam = False
    
if(spam):
    print("This is spam")
else:
    print("This is not spam")