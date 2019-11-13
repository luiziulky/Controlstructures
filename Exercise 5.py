n1 = float(input('first note: '))
n2 = float(input('second note: '))
average = (n1 + n2) / 2
if average == 10:
    print('APPROVED WITH DISTINCTION.')
elif average >= 7.0:
    print('APPROVED')
elif average < 7.0:
    print('DISAPPROVED')
