print('MISTERY')
print('Answer: y(yes) or n(no)')
a = str(input('Did you call to the victim? '))
b = str(input('Were you at the crime location? '))
c = str(input('Do you live near the victim? '))
d = str(input('Did you should to the victim? '))
e = str(input('Have you already worked with the victim?'))
s = [a,b,c,d,e]
cont = s.count('y')
if cont == 2:
    print('SUSPECT')
elif cont == 3 or cont == 4:
    print('ACCOMPLICE')
elif cont == 5:
    print('KILLER')
else:
    print('INNOCENT')