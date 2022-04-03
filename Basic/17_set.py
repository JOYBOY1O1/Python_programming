a = {1, 2, 3, 4, 1}  # cannot be repeated// collection of non repeteated items
b = {}
print("type of b={} is not set it is said to be: ", type(b))
print("\n", a)

z = set() #to create an empty set we use z=set()
print("z = set() is an empty set-->",type(z))
print(type(a))

#set methods

z.add(1)
z.add(4)
z.add(4)
z.add(5)
z.add(5)
# z.add([2,3,4]) throws error #list[] cannot be added in set because its changable
z.add((4,5,6)) #whereas tuple can be added in a set
print(z)
print(len(z))
z.remove(5)
print(z)
print("\n")
print("removes random element from the set z.pop()",z.pop())
print(z)
'''
#more commands

z.clear() empties the set
z.union({8,11})
z.intersection({8,11})

'''