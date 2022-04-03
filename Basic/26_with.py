#no need for f.close() in with function

with open('D:\CODE\Python\sample.txt','r') as f:
    a = f.read()
    
with open('new.txt','w') as f:
    a = f.write("writing using with open and f.write()")
print(a)