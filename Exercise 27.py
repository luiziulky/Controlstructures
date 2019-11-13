q1 = int(input('Strawberry[KG]: '))
q2 = int(input('Apples[KG]: '))
tot = q1 + q2
if q1 <= 5:
    tq1 = q1 * 2.50
elif q1 > 5:
    tq1 = q1 * 2.20
if q2 <= 5:
    tq2 = q2 * 1.80
elif q2 > 5:
    tq2 = q2 * 1.50
totp = tq1 + tq2
if tot > 8 or tot >= 25.0:
    vf = totp - (totp * 0.10)
    print(f'The value finalle {vf:.2f}')
else:
    print(f'The value finalle is {totp:.2f}')