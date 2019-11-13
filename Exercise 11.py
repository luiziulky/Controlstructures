s1 = float(input('Salary: '))
if s1 <= 280.0:
    value = s1 * 0.20
    s2 = s1 + value
    print(f'It was applied 20% of increase on your salary of R${s1}\n'
          f'the value of the increase was of R${value} and your salary finalle is R${s2}')
elif s1 < 700.0:
    value = s1 * 0.15
    s2 = s1 + value
    print(f'It was applied 15% of increase on your salary of R${s1}\n'
          f'The value of the increase was of R${value} and your salary finalle is R${s2}')
elif s1 < 1500.0:
    value = s1 * 0.10
    s2 = s1 + value
    print(f'It was applied 10% of increase on your salary of R${s1}\n'
          f'The value of the increase was of R${value} and your salary finalle is R${s2}')
elif s1 >= 1500.0:
    value = s1 * 0.05
    s2 = s1 + value
    print(f'It was applied 5% of increase on your salary of R${s1}\n'
          f'The value of the increase was of R${value} and your salary finalle is R${s2}')