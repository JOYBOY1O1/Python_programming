def max_no(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2
        else:
            return n3
       
m = max_no(23,32,21)
print("Max value is: " + str(m)) # cannot add string and integer together