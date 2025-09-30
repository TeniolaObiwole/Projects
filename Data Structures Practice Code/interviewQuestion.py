'''
Solve this
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

A = [0,1,2,3,4,5,6,7,8,9]
copyA = A.copy()
usedValues = []
target = 6

for i in A:
    for j in copyA:
        if j in usedValues:
            continue
        elif i+j == 6:
            print(i,j)
            usedValues.append(i)



print(usedValues)