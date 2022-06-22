# prints welcome message
print('Welcome to the Grade Sorter 9000!\n\n')

# Creates an empty Grades list then takes user input and sorts into numeric order
grades = []

print('Please give me 4 grades from 0 to 100:\n')
for i in range(4):
    g = int(input('Grade: '))
    grades.append(g)

print(f'Your Grades are: {grades}')

grades.sort()
grades.reverse()

print(f'Your grades from highest to lowest are: {grades}')

# removes the lowest 2 grades
print('Your lowest 2 grades are being removed...\n')
for x in range(2):
    removed_grade = grades.pop()
    print(f'Removed grade {removed_grade}')

print(f'\nYour remaining grades are: {grades}')
print(f'\nNice work, your highest grade is {grades[0]}')


