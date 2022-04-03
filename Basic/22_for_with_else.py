for i in range(10):
    print(i)
    if i==5 :
        break
else:
    print("inside else of for") #this does not print as loop does not completes
    
print("\n===========================================================================================\n")
for x in range(10):
    if x==5 :
        continue
    print(x)
else:
    print("Value of 5 gets skipped as continued for 5")
    
#pass is a null statement in python

z = 5
if z>0:
    pass #if do nothing
print("\nHello there!")