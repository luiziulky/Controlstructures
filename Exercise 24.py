import math
v1 = float(input('Enter the first value: '))
v2 = float(input('Enter the second value: '))
print('''OPERATIONS:
[1] Addition
[2] Subtraction
[3] Multiple
[4] Division''')
esc = int(input('Choose: '))
if esc == 1:
    s = v1 + v2
elif esc == 2:
    s = v1 - v2
elif esc == 3:
    s = v1 * v2
elif esc == 4:
    s = v1 / v2
if s % 2 == 0:
    a = 'pair'
else:
    a = 'odd'
if s > 0:
    n = 'positive'
elif s < 0:
    n = 'negative'
if math.ceil(s) == s:
    s = math.trunc(s)
    d = 'entire'
else:
    d = 'denary'
print(f'The result was {s},{a},{n} and {d}.')'''

