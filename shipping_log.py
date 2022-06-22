
# Username list and welcome message

username = ['liamj', 'jakeg', 'joshl', 'adamw', 'phillipjf', 'leela', 'zoidberg', 'farnsworth', 'hermesc', 'benderisthebest']

print("\nWelcome to Planet Express's shipping accounts program.")


# Username request loop

tries = 3
status = False

while status == False:
    for i in range(tries+1):
        if tries == 0:
            print('Too many attempted logins....Destroying all records. Goodbye.\n')
            exit()
        else:
            user = input('Username: ')
            user = user.lower()
            if user in username:
                print(f'Welcome {user}!\n')
                status = True
                break
            else:
                tries -=1
                print(f'User not found. Login attempts left: {tries}.\n')

# Stores the prices of shipping in variables, takes the user input and 
# charges the corresponding price, then prompts the user to proceed 
# with placing the order or cancelling 

print('\nCurrent shipping prices are as shown below: ')

a = 5.22
b = 5
c = 4.91
d = 4.78

print(f'Shipping orders 0 - 100: §{str(a)}')
print(f'Shipping orders 101 - 200: §{str(b)}')
print(f'Shipping orders 201 - 300: §{str(c)}')
print(f'Shipping orders 301 - 400: §{str(d)}')

num = int(input('How many items would you like to ship?: '))

if num > 0 and num <= 100:
    total = round(num * a, 2)
    print(f'\n\nTo ship {str(num)} items at §{str(a)} will cost: §{str(total)} in total.')
    answer = input('Would you like to place the order? (Y/N): ').lower()
    if answer.startswith('y'):
        print(f'Your order has been place, {user}, have a fanblorbluis day!\n\n')
        exit()
    elif answer.startswith('n'):
        print('Order cancelled, have a fantabulous day!\n\n')
        exit()
    else:
        print('Didnt recognise that answer.')


elif num > 100 and num <= 200:
    total = round(num * b, 2)
    print(f'\n\nTo ship {str(num)} items at §{str(b)} will cost: §{str(total)} in total.')
    answer = input('Would you like to place the order? (Y/N): ').lower()
    if answer.startswith('y'):
        print(f'Your order has been place, {user}, have a fanblorbluis day!\n\n')
        exit()
    elif answer.startswith('n'):
        print('Order cancelled, have a fantabulous day!\n\n')
        exit()
    else:
        print('Didnt recognise that answer.')


elif num > 200 and num <= 300:
    total = round(num * c, 2)
    print(f'\n\nTo ship {str(num)} items at §{str(c)} will cost: §{str(total)} in total.')
    answer = input('Would you like to place the order? (Y/N): ')
    if answer.startswith('y'):
        print(f'Your order has been place, {user}, have a fanblorbluis day!\n\n')
        exit()
    elif answer.startswith('n'):
        print('Order cancelled, have a fantabulous day!\n\n')
        exit()
    else:
        print('Didnt recognise that answer.')


elif num > 300 and num <= 400:
    total = round(num * d, 2)
    print(f'\n\nTo ship {str(num)} items at §{str(d)} will cost: §{str(total)} in total.')
    answer = input('Would you like to place the order? (Y/N):').lower()
    if answer.startswith('y'):
        print(f'Your order has been place, {user}, have a fanblorbluis day!\n\n')
        exit()
    else:
        print('Order cancelled, Goodbye!\n\n')
        exit()