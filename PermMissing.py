'''pseudocode
step 1: sort given array
step 2: find the max element
step 3: using the max element as a range, iterate through it and compare it's values to the values in the array.
step 4: if value not in array, return value as missing element
'''


A = [1]
A.sort()
maxElement = max(A)

for i in range(1,maxElement):
    if i not in A:
        print(i) 