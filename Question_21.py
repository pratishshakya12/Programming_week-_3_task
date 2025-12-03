# 21. Write a Python program to simulate a simple ATM with the following
# specifications:
#  Assume the card is valid (is_valid = True)
#  Initial account balance is 50000
#  Correct PIN is 123
#  After entering correct PIN, display the menu:
# 1. Withdraw
# 2. Check Balance
# 3. Exit
#  If user selects 1 then ask amount and deduct from balance
#  If user selects 2 then show current balance
#  If user selects 3 then print “Thank you for visiting”
#  Show proper messages for wrong PIN and invalid option Use nested if-else
# statements only
is_valid=True
balance=50000
pin=123
if is_valid==True:
    enter=int(input('Enter the 3 digit PIN:'))
    if enter==pin:
        print('1. Withdraw \n'
        '2. Check Balance \n'
        '3. Exit')
        answer=int(input('Enter the number for action:'))
        if answer==1:
            amount=int(input('Enter withdrawal amount:'))
            balance=balance-amount
        elif answer==2:
            print(balance)
        elif answer==3:
            print('Thankyou for visiting')
    else:
        print('Incorrect pin')
else:
    print('invalid card')       