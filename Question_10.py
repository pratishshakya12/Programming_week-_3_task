num1=int(input("enter first num:"))
num2=int(input("enter second num:"))
if num1==num2:
    print("equal")
    if num1>0:
        print("positive")
    elif num1<0:
        print("negetive")
    else:
        print("zero")
elif num1>num2:
    print("first num")
elif num1<num2:
    print("second num")
    