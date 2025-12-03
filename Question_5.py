#If usage < 100 units then cost Rs 5 per unit
#irst 100 units: Rs 5
 #Next units: Rs 8
#If usage is > 300 units:
# First 100: Rs 5
# Next 200: Rs 8
# Remaining: Rs 10
usage=int(input('Your electricity usage amount in bits :'))
if usage<100:
    cost=usage*5
elif usage>300:
    cost=500+1600+(usage-300)*10
else:
    cost=500+(usage-100)*8
print('Your Total is: ',cost)