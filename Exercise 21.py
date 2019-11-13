value = int(input('Withdrawal amount: '))
c = d = u = f = t = 0
while True:
    if value >= 100:
        value -= 100
        c += 1
    if value >= 50 and value < 100:
        value -= 50
        d += 1
    if 10 <= value < 50:
        value -= 10
        f += 1
    if 5 <= value < 10:
        value -= 5
        u += 1
    if 1 <= value < 5:
        value -= 1
        t += 1
    if value == 0:
        break
print(f'{c} notes of 100')
print(f'{d} notes of 50')
print(f'{f} notes of 10')
print(f'{u} notes of 5')
print(f'{t} notes of 1')
