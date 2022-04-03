#Tuple are immutable/ cannot be changed
t = () #empty tuple

# t = (1) is wrong way to declare single element
t = (1,) #tuple with single element

t = (1,2,3,4,1,1,2,5,1)

print(t.count(1))
print(t.index(5))
