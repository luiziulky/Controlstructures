price = list()
for c in range(0,3):
    price.append(float(input('Price: ')))
print(f'You should to buy the product worth {min(price)}')