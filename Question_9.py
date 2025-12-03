num1=int(input("enter a num:"))
if num1>0:
    print("positive")
    if num1%2==0:
        print("even")
    else:
        print("odd")
elif num1==0:
    print("zero")
elif num1<0:
    print("negetive number")