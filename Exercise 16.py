print('Bhaskara Formula')
while True:
    a = int(input('Value A: '))
    if a == 0:
        print('The equation is not of second grade')
        break
    b = int(input('Value B: '))
    c = int(input('Value C: '))
    delta = (b) ** 2 - (4 * a * c)
    if delta < 0:
        print('The equation has not real roots.')
        break
    elif delta == 0:
        print('The equation has only a real root that is 0.')
        break
    else:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        print(f'The roots are {x1} and {x2}')
        break
