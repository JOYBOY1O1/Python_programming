# Write a program to find the sum of first n natural numbers using a while loop.

n = int(input())
i = 1
sum = 0
while(i<n+1):
    sum = sum + i
    i = i+1
    
print(sum)