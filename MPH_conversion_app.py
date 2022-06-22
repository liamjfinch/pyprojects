# prints welcome message
print('Welcome to our MPH to MPS Converter!\n')

# takes user MPH and converts it to MPS
MPH = float(input('Miles Per Hour:'))

MPS = MPH*0.4474
MPS = round(MPS, 2)

# prints results
print(f'Your speed is {MPS} Metres Per Second!')