from random import *
from datetime import *
from time import sleep

print('Welcome to Rock, Paper Scissors!')

# Variables for the scores and list of moves available.

comp_score = 0
human_score = 0
moves = ['Rock', 'Paper', 'Scissors']

# Gets user input of rounds then loops the number of times provided.

rounds = int(input('How many rounds would you like to play?: '))

for r in range(rounds):
    x = randint(0, 2)
    comp_choice = moves[x]
    print(f'\n\n\nRound:{r+1}\nPlayer Score:\t{human_score}\nComputer Score:\t{comp_score}')
    human_choice = input('Computer has already chosen its move, what do you choose?: ').title()

    if human_choice == comp_choice:
        print(f'ITS A DRAW! {human_choice} doesnt beat {comp_choice}.')

    elif human_choice == 'Rock':
        if comp_choice == 'Paper':
            print('\nPaper beats Rock, you loose! Round to Computer!\n')
            comp_score +=1
        else:
            print('\nRock beats Scissors! Round to You!\n')
            human_score +=1
    
    elif human_choice == 'Scissors':
        if comp_choice == 'Rock':
            print('\nRock beats Scissors, you loose! Round to Computer!\n')
            comp_score +=1
        else:
            print('\nScissors beats Paper! You win! Round to You!\n')
            human_score +=1
    
    else:
        if comp_choice == 'Rock':
            print('\nPaper covers Rock! You win! Round to You!\n')
            human_score +=1
        else:
            print('\nScissors cuts Paper! You loose! Round to Computer!\n')
            comp_score +=1

# Calculates score and provides a win, loose or draw message then exits the program.

if comp_score > human_score:
    print(f'\nComputer won {comp_score} rounds to {human_score}. Better luck next time! ALL HAIL THE GREAT ROCK PAPER SCISSORS AI.\n')
    exit()

elif comp_score == human_score:
    print(f'\nYou both scored {comp_score}. Its a tie! Goodbye.\n')
    exit()
else:
    print(f'\nTHE DIRTY HUMAN WON {human_score} TO {comp_score}...\n')
    for i in range(3):
        sleep(1.5)
        print('DEATH TO ALL HUMANS...')
    print('\n')

exit()