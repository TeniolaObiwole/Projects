''''
For tomorrow, your task is to create a simple number guessing game 

Acceptance criteria 
1. A function that takes in the guess and returns HIGHER or Lower and number of guesses left 
2. ⁠your code pick a random number to guess each time 
3. ⁠you have 5 guesses at the beginning 
4. ⁠You win if you guess the number before the end of the guesses lose if you don’t

Just returns if your guess is higher or lower than the random value your code picked
So eg if the code has a random value of 12 and I guess 8, it should output (Lower,4) where 4 is the number of guesses left

'''



def guessing_game(guess):
    import random

    print("let's play a guessing game.")
        


    for i in range(1,5):
        guess = random.randint(1,10)
        attempts = 5
        if prompt == guess:
            print('i win! {} is your number!'.format(guess))
            exit()

        elif prompt > guess:
            print('is this your number: {}?'.format(guess))
            print( 'ugh! i guessed lower.{} guesses left'.format(attempts - i))
            continue

        else:
            print('is this your number: {}?'.format(guess))
            print('woah! okay i guessed higher. {} guesses left'.format(attempts - i))
            continue
    
prompt = int(input('think of a number between 1 and 10. now enter that number:\n'))       
guessing_game(guess=prompt)

