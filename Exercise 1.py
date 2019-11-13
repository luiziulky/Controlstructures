num = []
num.append(int(input('enter a number: ')))
num.append(int(input('enter a number: ')))
if num[0] == num[1]:
    print('The two numbers are equals')
else:
    print(f'the largest number is {max(num)}')

