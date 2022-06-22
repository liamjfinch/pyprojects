# prints welcome message
print('Welcome to the Tempurature Conversion App!\n')

# gets user input and converts
temp = float(input('What is the Degrees Farenheit?:'))

celsius = round((temp - 32)/1.80, 4)
kelvin = round(5/9*(temp - 32) + 273.15, 4)

# display results
print(f'\nDegrees Faranheit: {temp}')
print(f'Degrees Celcius: {celsius}')
print(f'Degrees Kelvin: {kelvin}\n')