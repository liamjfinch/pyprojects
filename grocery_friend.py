import datetime
from os import remove

food_list = ['Meat', 'Cheese']

# welcome message
print('\nWelcome to Grocery Friend!')

# variables which contain the date and time and prints it
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print(f'Current Date and Time: {day}/{month} {hour}:{minute}') 

# Takes user input and adds to food list then sorts them
print(f'\nThe current items in your Grocery List are: {food_list}\n')
for food in range(3):
    f = input('What food would you like to add to the list?: ').title()
    food_list.append(f)

print(f'\nYour updated list is: {food_list}')

food_list.sort()

print(f'Your sorted list: {food_list}')

# Program simulates shopping looping through user input 
# checking the list for the item and then removing from list
print('\nSimulating Shopping...')

while len(food_list) > 2:
        print('\nNumber of items on list:', len(food_list),'\n', food_list)
        purchased = input('What food did you just purchase?: ').title()
        for x in food_list:
            if purchased in food_list:
                print(f'{purchased} removed from list.')
                food_list.remove(purchased)
                break
            else:
                print(f'{purchased} not in list.')
                break

print('\nNumber of items on list:', len(food_list),'\n', food_list)

# Once the list reaches 2 items, the program lets the user know that their last item
# is out of stock and replaces the last item with their input
print(f'\n\nSorry, the store is out of {food_list[-1]}.')
food_list.pop()
replace = input('What food would you like instead?: ').title()
food_list.append(replace)
print(f'\n\n{replace} was added to your list...\nHere is your remaining items:', food_list)
