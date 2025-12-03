#the person is under 12, the ticket is free. If the person is between 12 and 60: if they
#have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs 200. If the
#person is above 60, they get a senior citizen discount, and then ticket costs Rs 100. 
age=int(input('Enter your age: '))
ticket_price=0
if age<12:
    ticket_price=0
elif age>60:
    ticket_price=ticket_price+100
else:
    member=str(input('Do you have a membership '))
    if member=='yes':
        ticket_price=ticket_price+150
    elif member=='no':
        ticket_price=ticket_price+200
print("Please pay amount : Rs",ticket_price)