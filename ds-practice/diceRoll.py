'''pseudocode
a dice only has six possible values, 1-6. the program is going to display any of the numbers 1 and 6 at random
step 1: import random module
step 2: ask user to roll the dice with a prompt.
step 3: using the random module, display any number from 1 - 6

'''
import random

def diceRoll():
    running = True

    while running:
        prompt = input('roll the dice? y/n\n').lower()

        if prompt == 'y':
            diceFace = random.randint(1,6)
            print(diceFace)

        elif prompt == 'n':
            print('ok')
            running = False
        
        else:
            print('incorrect input')

if __name__ == '__main__':
    diceRoll()