import math

# prints welcome message
print('\nWelcome to the Right Traingle Solver App!!\n')

# takes user input and calculates the hypotenuse and area
x_axis = float(input('What is the X axis of the Triangle?: '))
y_axis = float(input('What is the Y axis of the Triangle?: '))

hyp = round(math.sqrt((x_axis**2)+(y_axis**2)), 3)
area = round(0.5*x_axis*y_axis, 3)

# print results
print(f'\nFor a triangle with an X axis of {x_axis} and a Y axis of {y_axis}, the hypotenuse is {hyp}\n')
print(f'For a traingle with and X axis of {x_axis} and a Y axis of {y_axis}, the area is {area}', '\n')



