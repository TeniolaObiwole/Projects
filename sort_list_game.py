'''
So 4/10, for tomorrow I want you to write a code that can sort a list of numbers by the sum of their digits 
So basically you get a random list of like [133,175,201] and sorted they will be 201, 133 and 175
Because 3,7,13
'''

def sort_list(numbers:list):
    numDict= {}
    sortedList = []
    for i in numbers:
        numberSplit = [int(j) for j in str(i)]  
        #print(numberSplit)
        numberSum = sum(numberSplit)
        numDict[numberSum] = i

    numSorted = dict(sorted(numDict.items()))
    for number in numSorted.values():
        sortedList.append(number)
    
    return sortedList
    
    
tiny = sort_list([133,175,201])
print(tiny)

