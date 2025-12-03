num1=int(input("enter math:"))
num2=int(input("enter eng:"))
num3=int(input("enter sci:"))
num4=int(input("enter nep:"))
total_marks=num1+num2+num3+num4
percentage=total_marks/4
print(f"Your Total Marks is {total_marks}")
print(f"Your Percentage is {percentage}")
if percentage>70:
    print("DISTINCTION")
elif percentage>60:
    print("FIRST")
else:
    print("FAIL")
