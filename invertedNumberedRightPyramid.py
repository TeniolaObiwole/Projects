'''
Create a variable called count and set it to the value of N.
Create an outer loop and set it to the value of range N.
Create an inner loop and set it to the value of (1, count+1).
Print the numbers and set the argument end to space.
Subtract 1 from count after the inner loop.
Print a new line.
'''

N = 5
count = N

for i in range(N):
    for j in range(1,count+1):
        print(j, end = ' ')
    count -=1
    print()    