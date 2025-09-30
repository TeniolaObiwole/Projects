
# A = [4,1,3,2]

# def solution(input = A):
#     print(input)
#     sorted = input
#     sorted.sort()
#     if sorted[0] != 1:
#         return 0

#     for x in range(1, len(sorted)):
#         if input[x] - input[x - 1] != 1:
#             return 0
#     else:
#         return 1


# if __name__ == '__main__':
#    print(solution())

'''psuedocode
step 1: sort the list
step 2: if the first element is not 1 return 0
step 3: create a loop to iterate throught the array and compare the difference of it's values.
step 4: if it does not evaluate to one return 0
step 5: else return 1

'''

A = [4,1,3,2]

A.sort()

if A[0] != 1:
    print(0)

for i in range(1, len(A)):
    if A[i] - A[i-1] != 1:
        print(0)

else:
    print(1)
