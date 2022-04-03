# list --> ordered
a =[1,2,3,4,5]
print(a)
print(a[-1])
print(a[3:])

#editiable/ changeable
a[0]=99
print(a)
print("\n")

#list slicing

friends = ["Apple", "Akash", "Rohan", 7, False ]
print(friends)
print("\n")

#list methods

l1 =[2,43,1,3,99,434,32,2]
print("List = ",l1)
print("\n")

l1.sort()
print("sorting ascending l1.sort()",l1)
print("\n")

l1.reverse()
print("sorting descending l1.reverse()",l1)
print("\n")

l1.append(989)
print("adding number(989) at the end of the list l1.append(989)",l1)
print("\n")

l1.insert(3,8)
print("Inseting 8 at 3 index l1.insert(3,8): ",l1)
print("\n")

l1.pop(3)
print("Will delete the element at index 3--> l1.pop(3)",l1)
print("\n")

l1.remove(2)
print("Will remove the first same element from index l1.remove(2)",l1)