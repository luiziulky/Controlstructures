l = ['Filé Duplo','Alcatra','Picanha']
print('HIPERMERCADO TABAJARA')
print('''Type of beef:
[1] Double fillet
[2] Rump
[3] Filet steak''')
type = int(input('Type: '))
option = l[type-1]
qb = int(input('Amount[KG]: '))
if type == 1:
    if qb <= 5:
        tf  = 4.90 * qb
    else:
        tf = 5.80 * qb
elif type == 2:
    if qb <= 5:
        tf = 5.90 * qb
    else:
        tf = 6.80 * qb
elif type == 3:
    if qb <= 5:
        tf = 6.90 * qb
    else:
        tf = 7.80 * qb
print('''TYPE OF PAYMENT:
[1] Tabajara Card
[2] Credit Card
[3] Money''')
pay = int(input('Type: '))
p = ['Tabajara Card','Credit Card','Money']
o = p[pay-1]
if pay == 1:
    vd = tf * 0.10
    vf = tf - vd
else:
    vf = tf
    vd = 0
d = dict()
d['Type'] = option
d['Amount'] = qb
d['Total Price'] = tf
d['Pay Type'] = o
d['Discount Value'] = vd
d['Value Payment'] = vf
for k,i in d.items():
    print(f'{k} has value {i}')