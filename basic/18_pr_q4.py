'''
What will be the length of the following set S:
S = Set()
S.add(20)
S.add(20.0)
S.add(“20”)
'''
S = set()
S.add(20)
S.add(20.0)
S.add("20")
print("Length of set() =",len(S))
print("Length of set {20,20.0,'20'} = 2 because 20 == 20.0 is same")