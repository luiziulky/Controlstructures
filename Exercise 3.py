sexo = str(input('sex [M/F]: ')).strip().upper()[0]
if sexo in 'MF':
    print('valid gender')
else:
    print('Invalid gender')