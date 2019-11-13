n1 = float(input('Note 1: '))
n2 = float(input('Note 2: '))
n3 = float(input('Note 3: '))
average = (n1 + n2 + n3) / 3
if average == 10.0:
    print('Approved with distinction.')
elif average >= 7.0:
    print('Approved')
else:
    print('Disapproved')
