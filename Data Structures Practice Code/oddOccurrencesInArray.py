'''
pseudocode
with a dictionary
1. create an empty dictionary(elementCount)
2. for i in listOfIntegers:
        elementCount[i] = elementCount.get(i,1) +1
3. for key, value in elementCount.items:
        if value % 2 == 0:
            return value    

with 2 lists                       
step1: create 2 lists: uniqueList and duplicateList
step 2: for i in originalList:
            if i not in uniqueList:
                uniqueList.append(i)
            elif i not in duplicateList:
                duplicateList.append(i)
step 3: for j in originalList:
            if j not in duplicateList:
                print(j)

with count method
step 1: for i in originalList:
            n = originalList.count(i)
            if n%2 == 1:
                print(n)
           
'''
#with a dictionary
A = [9,3,9,3,9,7,9]
elementCount = {}

for i in A:
    elementCount[i] = elementCount.get(i,0) +1
for key, value in elementCount.items():
    if value % 2 != 0:
        print(key)


#with 2 lists
uniqueList = []
duplicateList = []

for i in A:
    if i not in uniqueList:
            uniqueList.append(i)
    elif i not in duplicateList:
            duplicateList.append(i)

for j in A:
       if j not in duplicateList:
              print(j)

#with the count method              
for i in A:
    n = A.count(i)
    if n%2 == 1:
        print(i)