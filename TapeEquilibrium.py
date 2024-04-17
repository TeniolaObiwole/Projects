'''pseudocode
step 1: create two empty variables, firstPart & secondPart & an empty list absoluteDifference.
step 2: create a for loop to iterate through the array.
step 3: assign to firstPart the sum of elements before P (A[0], A[1], ..., A[P − 1]).
step 4: assign to secondPart the sum of all elements starting from P till the end (A[P], A[P + 1], ..., A[N − 1]).
step 5: append to absoluteDifference the absolute difference of firstPart and secondPart.
step 6: return the smallest element in absoluteDifference
'''

A = [3,1,2,4,3]

firstPart = None
secondPart = None
absoluteDifference = []

for P in range(len(A)):
    if P == 0:
        continue
    else:
        firstPart = sum(A[0:P])
        secondPart = sum(A[P:])
        absoluteDifference.append(abs((firstPart )- (secondPart)))
        
print(min(absoluteDifference))
# print(absoluteDifference)

    
