# Write a program to find out whether a file is identical and matches the content of another file.

file1 = "copy_sample.txt"
file2 = "sample.txt"

with open(file1) as f:
    f1 = f.read()

with open(file1) as f:
    f2 = f.read()

if f1==f2:
    print("files are identical")
else:
    print("files are non identical")