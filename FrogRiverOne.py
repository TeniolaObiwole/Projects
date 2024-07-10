'''pseudocode
step 1: create an empty dictionary to store the leaf position(list elements) and time(element index).
step 2: iterate through the list and assign to the dictionary it's position as key and time as value.
step 3: sort the dictionary keys 

step 1: create an empty list to store the position count 
step 2: using x to create a range make a for loop to iterate through the list.
step 2: check the list for any value in x.
step 3: if value is present, add the values index to count list, when loop is complete print out the last item of the list.
step 4: else print -1.

'''

# A = [1,3,1,4,2,3,5,4]

def solution( X, A):
    count = []
    try:
        for i in range(1,X+1):
            if i in A:
                count.append(A.index(i))
            else: 
                return -1
        return max(count)
    except TimeoutError:
        return -1
print(solution(X = 3, A = [1, 3, 1, 3, 2, 1, 3]))

     