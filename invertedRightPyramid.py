'''
Create a variable called count and assign to it the value of range N.
Create outer loop and set it to the value of N.
Create an inner loop and set it to the value of range count.
Print the star.
Subtract 1 from count.
Add a print statement after the inner loop.
'''

N = 5
count = N

for i in range(N):
    for j in range(count):
        print('*', end = ' ')
    count -=1
    print()
    