time=int(input("Time period of service:"))
salary=int(input("Enter your salary:"))
if time<6:
    final_salary=salary*1.05
elif time>10:
    final_salary=salary*1.1
else:
    final_salary=salary*1.05
print("Your final salary is: ",final_salary)