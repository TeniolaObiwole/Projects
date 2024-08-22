'''
Problem Statement: Given an integer N, print a Right-Angled Number Pyramid.

Solution
Initialize nested loops to make pyramid.
Outer loop is set to range N.
Create a variable count and assign to it the number 2.
Set inner loop to range count.
Print the current value of the iterator and set print parameter, end to a space.

'''

N = 9
count = 2

for i in range(N):
    for j in range(1,count):
        print(j, end = ' ')
    print()
    count +=1
    
 
 