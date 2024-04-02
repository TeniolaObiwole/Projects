'''
1. create copy of list (L)
2. for rotation in K(where k is the number of rotations)
    a. insert o at index 1
3. for index in L:
    a. if index >= (len(original_array))
    b. assign value to the index represented by index-(len(original_array))
4. splice to the len(original_array)
'''

A = [3, 8, 9, 7, 6]
K = 1
L = A.copy()
for i in range(K):
    L.insert(0,0)
    #print(listCopy)

for j in range(len(L)):
    if j >= (len(A)):
        L[j-len(A)] = L[j]
        #print(L)
L = L[:len(A)]

print(L)

