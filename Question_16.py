cost=int(input("Enter the cost price of the bike: "))
if cost>100000:
    tax=cost*0.15
elif cost>50000 and cost<100000:
    tax=cost*0.10
else: 
    tax=cost*0.05
print(f"Road tax :Rs{tax}")