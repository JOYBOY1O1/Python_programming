#use open function to read the content of the file\
f = open('D:\CODE\Python\sample.txt','r')
data = f.read()
data1 = f.readline()
# data = f.read(5) reads first 5 characters from file
print(data)
print(data1)#reads first line
f.close()
'''
r   - open for reading
w   - open for writing
a   - open for appending
+   - open for updating

'rb'- open for read in binary mode
'rt'- open for read in text mode
'''

#write in a file


f = open('D:\CODE\Python\sample_new.txt','w')
f.write("This is new file created using f=open('sample_new.txt','w')\nand new line written using f.write() function")
f.close()
f = open('D:\CODE\Python\sample_new.txt','a')
f.write(" I am appending")#adds at the end
f.close()