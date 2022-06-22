
parties = ['Labour', 'Conservative', 'Liberal Democrat', 'Green', 'Scottish National Party']

print("Welcome to Voter Registration.")
name = input('Name: ').title()
age = int(input('Age: '))

if age < 18:
    print('You are not old enough to vote, Goodbye.')
    exit()
else:
    print(f'\nHello {name}.\n')
    print('These are the list of parties to vote for:')
    for p in parties:
        print('-', p)

status = False
while status == False:
    choice = input('\nWhich party would you like to vote for: ').title()
    
    if choice in parties:
        print(f'Congratulations {name}, you have voted for the {choice} Party. Have a great day!')
        status = True
    else:
        print(f'The {choice} Party is not an available party, please try again.')

