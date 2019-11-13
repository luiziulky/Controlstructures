value = float(input('Value/hour: '))
hours = int(input('Hour/month: '))
gross = value * hours
if gross <= 900.0:
    d = 0
elif gross <= 1500.0:
    d = 5
    ir = (gross * 0.05)
elif gross <= 2500.0:
    ir = (gross * 0.10)
    d = 10
else:
    ir = (gross * 0.20)
    d = 20
inss = gross * 0.10
fgts = gross * 0.11
tot = ir + inss + fgts
sl = gross - tot
print(f'gross salary: ({value} * {hours})                      :R${gross}')
print(f'(-) IR({d}%)                                    : R${ir:.2f}')
print(f'(-) INSS(10%)                                  : R${inss:.2f}')
print(f'FGTS(11%)                                      : R${fgts:.2f}')
print(f'Total discounts                                : R${tot:.2f}')
print(f'Net salary                                     : R${sl:.2f}')