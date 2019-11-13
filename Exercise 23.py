import math
num = float(input('Enter a number: '))
if math.ceil(num) == num:
    print('This number is entire.')
else:
    print('This number is denary.')