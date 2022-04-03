# Write a python program to rename a file to “renamed_by_python.txt.”
import os

oldname ="sample.txt"
newname= "renamed_by_python.txt"
with open(oldname) as f:
    c = f.read()
with open(newname,"w") as f:
    f.write(c)
os.remove(oldname)