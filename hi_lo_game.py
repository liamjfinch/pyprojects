from random import *

# welcomes the user, asks for their name and generates a random number
# sorting it in a variable to be checked later in the game loop

print("\n\nWelcome to Hi Low! The number guessing game!")
name = input('\nWhat is your name?: ').title()

number = randint(1, 20)

print(f'\nOkay {name}, im thinking of a number between 1 and 20. Can you guess what it is?')


# keeps a variable with the number of guesses and creates a game loop, ending once all guesses are used
# or when the user inputs the correct number.

num_guess = 5

while num_guess > 0:

    guess = int(input('\n\nWhat number am i thinking of?: '))
        
    if guess == number:
        print(f'Well done! {str(number)} was the number i was thinking of!')
        print('Thank you for playing!')
        exit()
        
    elif guess > number:
        if num_guess > 1:
            print(f'Wrong! The number im thinking of is less than {str(guess)}')
            num_guess -=1
            print(f"You only have {num_guess} guess's left")
        else:
            num_guess -=1

        
    elif guess < number:
        if num_guess > 1:
            print(f"Wrong! The number im thinking of is more than that. Try again!")
            num_guess -=1
            print(f"You only have {num_guess} guess's left")
        else:
            num_guess -=1


# Prints the loosing message and exits the program

print(f'Too bad, you run out of guesses, the number i was thinking of was {str(number)}')
exit()