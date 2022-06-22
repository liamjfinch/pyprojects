import random


# welcome message
print('Welcome to the best coinflip app ever made.\n\n')
flips = int(input('How many times would you like to flip the coin?: '))
answer = input('Would you like to see the result of each individual flip?: ').lower()

# for loop generates the coin flips and calculates the percentage of total flips 
heads = 0
tails = 0

for times in range(flips):
    if answer.startswith('y'):
        x = random.randint(0, 1)
        if x == 0:
            heads += 1
            print('Heads')
        else:
            tails +=1
            print('Tails')
    else:
        x = random.randint(0, 1)
        if x == 0:
            heads +=1
        else:
            tails +=1

h_percent = round(heads / flips, 4)
t_percent = round(tails / flips, 4)

# prints results

print('Results:')
print(f'Side:\tCount:\tPercentage:')
print(f'Heads\t{heads}\t{h_percent*100}%')
print(f'Tails\t{tails}\t{t_percent*100}%')
