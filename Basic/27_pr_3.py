# Write a program to make a copy of a text file “sample.txt.”

with open("sample.txt","r") as f:
    content = f.read()
    
with open("copy_sample.txt","w") as f:
    f.write(content)