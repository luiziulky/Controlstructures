liter = int(input('Liters sold: '))
print('''Type of fuel:
[A]- alcohol
[G]- gasoline''')
type = str(input('Type: '))
if type == 'a':
    if liter <= 20:
        a1 = liter * (1.90 - (1.90 * 0.03))
        print(f'The value is R${a1:.2f}')
    else:
        a2 = liter * (1.90 - (1.90 * 0.05))
        print(f'The value is R${a2:.2f}')
elif type == 'g':
    if liter <= 20:
        g1 = liter * (2.50 - (2.50 * 0.04))
        print(f'The value is R${g1:.2f}')
    else:
        g2 = liter * (2.50 - (2.50 * 0.06))
        print(f'The value is R${g2:.2f}')