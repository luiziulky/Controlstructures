n = list()
for c in range(0,3):
    n.append(int(input('Enter a number: ')))
n.sort(reverse=True)
print(f'Decrescent order: {n}')