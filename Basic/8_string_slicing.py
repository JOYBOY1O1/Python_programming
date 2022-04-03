print("\n")
greet = "Good morning, "
name = "Joy khulbe"
a = greet + name
print(a)
print(a[0])

print("printing from index 0 to 10 --> ",a[0:10],"\n" )  # Length starts from 0 to (length-1)
print("printing from index a[:5] --> ",a[:5],"\n")
print("printing from index a[0:] --> ",a[0:],"\n")
print("printing from index 14 to 24 --> ",a[14:24],"\n")
print("printing from index (-24 == 0 )at index to (-6 == 14) --> ",a[-24:-6],"\n")

# G   o   o   d     m   o   r   n   i   n   g   ,     J   o   y     k   h   u   l   b   e 
# 0   1   2   3  4  5   6   7   8   9   10  11  12 13 14  15  16 17 18  19  20  21  22  23
#-24 -23 -22 -21-20-19 -18 -17 -16 -15 -14 -13 -12-11-10 -9  -8 -7 -6  -5  -4  -3  -2  -1
# you can access specific index of string but cannot chnage it

#slicing with skip value

word = "breathtaking"

print("Values from 0 to 12 with skip value of 3",word[0: :3]) #blank in between means till end
# bati