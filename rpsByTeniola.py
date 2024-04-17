'''
It’s a rock paper scissors game, you against computer.
1. You need to be able to decide between best out of 3 or best out of 5.
2. ⁠You need to be able to show history of the past 20 games.
'''
import random

def play():
    
    options = ('rock', 'paper', 'scissors')

    running = True
    count = 1
    history = {}

    while running:

        computer = random.choice(options)
        player = None
        gamePlay = {'user':0, 'computer':0}
        
        
        while player not in options:
            player = input('Rock, Paper, Scissors?\n').lower()

        if player == computer:
            print(computer,'\ntie!')
        elif player == 'rock' and computer == 'scissors':
            gamePlay['user'] +=1
            print(computer, '\nyou win!')
        elif player == 'paper' and computer == 'rock':
            gamePlay['user'] +=1
            print(computer, '\nyou win!')
        elif player == 'scissors' and computer == 'paper':
            gamePlay['user'] +=1
            print(computer, '\nyou win!')
        else:
            gamePlay['computer'] +=1
            print(computer,'\nyou lose!')

        history['round {}'.format(count)] = gamePlay
        count +=1
        if count == 20:
            history = {}

        if not input('play again? y/n \n').lower() == 'y':
            print(history,'nice game!')
            running = False

    

    
if __name__ == '__main__':
    play()
