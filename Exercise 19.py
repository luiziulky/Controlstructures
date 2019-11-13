num = int(input('Enter a number: '))
if 100 <= num < 1000:
    c = num // 100
    r = num % 100
    d = r // 10
    r = r % 10
    if c > 1 and d > 1 and r > 1:
        print(f'{num} = {c} hundreds, {d} dozens and {r} units.')
    elif c <= 1 and d > 1 and r > 1:
        print(f'{num} = {c} hundred, {d} dozens and {r} units.')
    elif d <= 1 and c > 1 and r > 1:
        print(f'{num} = {c} hundreds, {d} dozen and {r} units.')
    elif r <= 1 and c > 1 and d > 1:
        print(f'{num} = {c} hundreds, {d} dozens and {r} unit.')
    elif c <= 1 and d <= 1 and r > 1:
        print(f'{num} = {c} hundred, {d} dozen and {r} units.')
    elif d <= 1 and r <= 1 and c < 1:
        print(f'{num} = {c} hundreds, {d} dozen and {r} unit.')
    elif c <= 1 and r <= 1 and d > 1:
        print(f'{num} = {c} hundred, {d} dozens and {r} unity.')
    elif c <= 1 and r <= 1 and d <= 1:
        print(f'{num} = {c} hundred, {d} dozen and {r} unity.')
    elif c > 1 and d <= 1 and r <= 1:
        print(f'{num} = {c} hundreds, {d} dozen and {r} unity.')
    elif c > 1 and d <= 1 and r <= 1:
        print(f'{num} = {c} hundreds, {d} dozen and {r} unity.')
    elif c <= 1 and d <= 1 and r <= 1:
        print(f'{num} = {c} hundred, {d} dozen and {r} unity.')
elif num < 99:
    d = num // 10
    u = num % 10
    if d > 1 and u > 1:
        print(f'{num} = {d} dozens and {u} unitys.')
    elif d > 1 and u <= 1:
        print(f'{num} = {d} dozens and {u} unity.')
    elif d <= 1 and u > 1:
        print(f'{num} = {d} dozen and {u} unitys.')
    elif d <= 1 and u <= 1:
        print(f'{num} = {d} dozen and {u} unity.')