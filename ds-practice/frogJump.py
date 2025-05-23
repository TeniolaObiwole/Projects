'''pseducode
int x = initial position
int y = frog will jump a distance greater than or equal to this position
int d = fixed distance 

1. initialJump = x + d
2. finalJump = initial jump
3. jumpCounter = 1
2. while True: 
    if finalJump is not >= y:
            finalJump += d
            jumpCounter +=1
3. return finalJump and jumpCount
'''

X = 10
Y = 85
D = 30

def Solution(X,Y, D):
    initialJump = X+D
    finalJump = initialJump
    jumpCounter = 1
    while True:
        if not finalJump >= Y:
            finalJump += D
            jumpCounter +=1
            #print(finalJump, jumpCounter)
        else:
            break
    return jumpCounter

print(Solution(X,Y,D))

#Solution(X,Y,D)
