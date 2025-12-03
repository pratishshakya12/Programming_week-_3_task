a=int(input('The number of students in the first class:'))
b=int(input('The number of students in the second class:'))
c=int(input('The number of students in the third class:'))
if a%2==0:
    a=a
else:
    a=a+1
if b%2==0:
    b=b
else:
    b=b+1
if c%2==0:
    c=c
else:
    c=c+1
total=(a+b+c)/2
print('Total no of desks needed is ',total)
