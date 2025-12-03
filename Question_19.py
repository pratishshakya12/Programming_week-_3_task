age=int(input('Enter your age: '))
if age>=18:
    degree=str(input('Do you have a degree: '))
    if degree=='yes':
        work=int(input('Enter your work experience in years: '))
        if work>3:
            print('Highly eligible')
        elif work==3 or work==2 or work==1:
            print('Eligible')
        else: 
            print('Under review')
    else:
        print("Ineligible")
else:
    print("Ineligible")