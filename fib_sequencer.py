
num = int(input('How many of the digits of the Fibonacci Sequence would you like to itterate?: '))

# Iterates through the fibonacci sequence any number of times
fib = [1, 1]
for i in range(num):
    new_fib = fib[-1]+fib[-2]
    fib.append(new_fib)
    print(fib[i])

# Works out the Golden Ratio
print('\nGolden Ratio: \n')
g_ratio = []
for i in range(len(fib)-2):
    ratio = fib[i+1]/fib[i]
    g_ratio.append(ratio)
    print(g_ratio[i])