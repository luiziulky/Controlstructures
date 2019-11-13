print('-+' * 15)
print('Verication of a triangle')
print('-+' * 15)
l1 = float(input('Side 1: '))
l2 = float(input('Side 2: '))
l3 = float(input('Side 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Equilateral Triangle.')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Isosceles Triangle.')
    else:
        print('Scalene Triangle.')
else:
    print('It is not possible to form a triangle.')