from words import word_list
import random

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    print(word)
    guessed = False
    word_completion = '_ ' * len(word)
    guessed_letters = []
    guessed_words = []
    incorrect_tries = 6

    print("Let's play Hangman!")    
    print(word_completion)

    while not guessed and incorrect_tries > 0:
        guess = input('Guess a letter:\n').upper()
        if len(guess) == 1 and guess.isalpha:
            if guess in guessed_letters:
                print("You've guessed {} already.".format(guess))
            elif guess not in word:
                print('Incorrect guess.Try again.')
                incorrect_tries -=1
                guessed_letters.append(guess)
            else:
                print('Correct guess!')
                guessed_letters.append(guess)
                word_as_a_list = list(word_completion.replace(' ',''))
                
                indices = [i for i, letter in enumerate(word) if letter == guess ]

                for index in indices:
                    word_as_a_list[index] = guess

                print(word_as_a_list)
                word_completion = ' '.join(word_as_a_list)
            
                if '_' not in word_completion:
                    guessed = True
        elif len(word) == len(guess) and guess.isalpha:
            if guess in guessed_words:
                print("You've guessed {} already.".format(guess))
            elif guess != word:
                print('Incorrect guess')
                guessed_word.append(guess)
                incorrect_tries-=1
            else:
                #print(word)
                print("You've guessed correctly!")
                guessed = True
        else:
            print('Invalid guess.')

        print (display_hangman(incorrect_tries))
        print(word_completion)
    if guessed == True:
        print('You win!')



def display_hangman(incorrect_tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[incorrect_tries]


def main():
    word = get_word(word_list)
    play(word)
    if input('Play again? Y/N').upper() == 'Y':
        word = get_word()
        play(word)

if __name__ == '__main__':
    main()

#print(word_list)
