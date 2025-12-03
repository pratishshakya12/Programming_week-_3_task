num1=int(input('Enter the first number'))
num2=int(input('Enter the second number'))
num3=int(input('Enter the third number'))
greater=0
if num1>num2 and num1>num3:
    greater=greater+num1
elif num2>num1 and num2>num3:
    greater=greater+num2
elif num3>num2 and num3>num1:
    greater=greater+num3
str(greater)
print(f"The greatest number is: {greater}")