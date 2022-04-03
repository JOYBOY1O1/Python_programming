# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.
favlang = {}
a = input("1 Enter your fav language adele: ")
b = input("2 Enter your fav language buck: ")
c = input("3 Enter your fav language chuck: ")
d = input("4 Enter your fav language duck: ")
favlang['adele'] = a
favlang['buck'] = b
favlang['chuck'] = c
favlang['duck'] = d

print(favlang)

# If the names of 2 friends are the same; what will happen to the program in Program 6?
'''
favlang['adele'] = a
favlang['buck'] = b
favlang['chuck'] = c
favlang['chuck'] = d
2 nams are same chuck and chuck so the output will be

input:
1 Enter your fav language adele: python 
2 Enter your fav language buck: c++
3 Enter your fav language chuck: java
4 Enter your fav language chuck: c
output:
{'adele': 'python ', 'buck': 'c++', 'chuck': 'c'}
'''