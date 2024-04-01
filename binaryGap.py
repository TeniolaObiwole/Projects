def binaryGap(N : int):
    binNumber = bin(N) [2:]
    print(binNumber)
    count = 0
    maxCount = 0

    for i in binNumber:
        if int(i) == 0:
            count +=1
            print('count:',count)
        elif int(i) == 1:
            maxCount = max(maxCount, count)
            count = 0
            print('maxCount:',maxCount)
        else:
            print('invalid input')
    
    return maxCount

print(binaryGap(90))
    