model = 'dd/mm/aaaa'
while True:
    date = str(input('Enter a date of today: ')).strip()
    if len(date) == len(model):
        print(f'{date} is a valid date.')
        break
    else:
        print('Invalid date.Try again.')