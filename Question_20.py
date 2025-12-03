age=int(input('Enter your age: '))
gender=(input('Enter your gender (M/F): '))
days=int(input('Enter your working days: '))
if age>=18 and age<30:
    if gender=='M':
        wage=days*700
    elif gender=='F':
        wage=days*750
elif age>=30 and age<=40:
    if gender=='M':
        wage=days*800
    elif gender=='F':
        wage=days*850
print(' Your Wage Amount is: ',wage)
