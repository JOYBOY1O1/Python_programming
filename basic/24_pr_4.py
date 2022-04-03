#Write a python function to remove a given word from a string and strip it at the same time.

def strip(string,word):
    newstr = string.replace(word, "")#blank se replace kara word ko
    return newstr.strip()
this ="     harry is a good boy      "    
n = strip(this, "harry")
print(n)