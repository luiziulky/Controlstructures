l = ['Sunday','Monday','tuesday','Wednesday','Thursday','Friday','Saturday']
print('DAYS OF THE WEEK')
while True:
    num = int(input('Enter a number: '))
    if 0 < num < 8:
        print(l[num-1])
        break
    else:
        print('Invalid value')