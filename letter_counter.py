# Prints welcome message
print('Welcome to the fantastical, marveloso, splendido Letter Counter 420!\n')

# gets user name and capitalizes it
name = input('What is your name?:').title().strip()

# message that welcomes the user and uses their name provided
print(f"Hello {name}!\n")

# message that prints the aim of the program
print('The aim of this program to to count the amount of times a letter appears in a message.\n')

# gets user input and standardizes
message = input('What is the message you would like to use?:').lower()
letter = input('\n\n...and the letter you would like to count?:').lower()

# the program takes the input and uses the .count() function to count the amount of 
# times the variable: letter, appears in the variable: message.
# the program also prints a message incase the letter does not appear in the message
letter_count = message.count(letter)
if letter_count == "0":
    print(f"The letter {letter} is not in this message!")
    quit

# message to indicate the results
print(f'\nThe letter {letter} appears {letter_count} times!')