# Welcome message
print('Welcome to my Multiplication/Exponent Table App\n')

# Gets user input and performs the calculations
name = input('What is your name?: ')
number = float(input('\nWhat is you number?: '))

print (f'\n\nMultiplication Table for {number}:\n\n')

for i in range(1, 10):
    x = round(i * number, 4)
    print(f'{i} * {number} = {x}')
    
print(f'\n\nExponential Table for {number}:\n\n')

for j in range(1, 10):
    y = round(number ** j, 4)
    print(f'{j} ** {number} = {y}')

# Prints final message
message = name.title() + ", Math is cool!"
print('\n', message, '\n', message.lower().strip(), '\n', message.title().strip(), '\n', message.upper().strip())
