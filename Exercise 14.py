student = {}
n1 = float(input('Note 1:'))
n2 = float(input('Note 2:'))
average = (n1 + n2) / 2
if average < 4.0:
    s = 'DISAPPROVED'
    c = 'E'
elif 4.0 <= average < 6.0:
    s = 'DISAPPROVED'
    c = 'D'
elif 6.0 <= average < 7.5:
    s = 'OKAY'
    c = 'C'
elif 7.5 <= average < 9.0:
    s = 'OKAY'
    c = 'B'
else:
    s = 'OKAY'
    c = 'A'
student[n1] = (n1,n2,average,c,s)
for k,v in student.items():
    print(f'Note:      {v[0:2]}')
    print(f'Average:   {v[2]}')
    print(f'Concept:   {v[3]}')
    print(f'Situation: {v[4]}')