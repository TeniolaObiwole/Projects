'''
step1: create 2 lists: uniqueList and duplicateList
step 2: for i in originalList:
            if i not in uniqueList:
                uniqueList.append(i)
            elif i not in duplicateList:
                duplicateList.append(i)
step 3: for j in originalList:
            if j not in duplicateList:
                print(j)
            
'''

A = [9,3,9,3,9,7,9]
B = []

for i in A:
    n = A.count(i)
    if n < 2:
        print(i)
       

