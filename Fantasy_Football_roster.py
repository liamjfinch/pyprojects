

# Welcome message.

print('\nWelcome to Fantasy Football Draft!')



# Creates an empty dictionary of lists to store players.

roster = {
    'Goalkeeper': [],
    'Wing-Backs': [],
    'Centre Backs': [],
    'Midfielders': [],
    'Wingers': [],
    'Forwards': []
    }



# While loop takes user input and adds it to the roster.

number_of_players = 0

print('Lets fill in the players for your 4-4-2:\n')
while number_of_players < 11:

    gk = input('\nGoalkeeper: ').title()
    print(f'{gk} added to the roster.')
    roster['Goalkeeper'].append(gk)
    number_of_players +=1

    wb1 = input('\n\nLeft Wingback: ').title()
    roster['Wing-Backs'].append(wb1)
    wb2 = input('Right Wingback: ').title()
    roster['Wing-Backs'].append(wb2)
    print(f'{wb1} and {wb2} added to roster.')
    number_of_players +=2

    cb1 = input('\n\nLeft Centreback: ').title()
    roster['Centre Backs'].append(cb1)
    cb2 = input('Right Centreback: ').title()
    roster['Centre Backs'].append(cb2)
    print(f'{cb1} and {cb2} added to roster.')
    number_of_players +=2

    m1 = input('\n\nLeft Centre Midfield: ').title()
    roster['Midfielders'].append(m1)
    m2 = input('Right Centre MIdfield: ').title()
    roster['Midfielders'].append(m2)
    print(f'{m1} and {m2} added to roster.')
    number_of_players +=2

    w1 = input('\n\nLeft Wing: ').title()
    roster['Wingers'].append(w1)
    w2 = input('Right Wing: ').title()
    roster['Wingers'].append(w2)
    print(f'{w1} and {w2} added to roster.')
    number_of_players +=2

    s1 = input('\n\nLeft Forward: ').title()
    roster['Forwards'].append(s1)
    s2 = input('Right Forward: ').title()
    roster['Forwards'].append(s2)
    print(f'{s1} and {s2} added to roster.')
    number_of_players +=2



# Generates the team and displays it within the players positions.

print('\n\nGenerating team...\n\n')
team_name = input('What is your team name?: \n').title()
print(f'{team_name}:')
print('\t\t','  ',roster['Goalkeeper'][0],'\n\n', roster['Wing-Backs'][0],'\t', roster['Centre Backs'][0],'\t', roster['Centre Backs'][1],'\t', roster['Wing-Backs'][1],'\n\n',
        roster['Wingers'][0],'\t', roster['Midfielders'][0],'\t', roster['Midfielders'][1],'\t', roster['Wingers'][1],'\n\n',
        '\t\t', roster['Forwards'][0],'  ', roster['Forwards'][1])



# Lets the user know that one of their players are injured and asks them to replace them,
# then takes the imput and replaces them in the roster and re prints the new team.

injured_player = roster['Midfielders'][0]

print(f'\nOh no! It seems {injured_player} is injured!')
number_of_players -=1
print(f'{team_name} only has {number_of_players} players.')
added_player = input('Who would you like to replace him with?: ').title()
roster['Midfielders'][0] = added_player
print(f'{added_player} has replaced {injured_player}')
number_of_players +=1
print(f'{team_name} now has {number_of_players} players. Best of luck {added_player}!\n\n')

print(f'{team_name}:')
print('\t\t','  ',roster['Goalkeeper'][0],'\n\n', roster['Wing-Backs'][0],'\t', roster['Centre Backs'][0],'\t', roster['Centre Backs'][1],'\t', roster['Wing-Backs'][1],'\n\n',
        roster['Wingers'][0],'\t', roster['Midfielders'][0],'\t', roster['Midfielders'][1],'\t', roster['Wingers'][1],'\n\n',
        '\t\t', roster['Forwards'][0],'  ', roster['Forwards'][1])
