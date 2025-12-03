planets={1:(0.38),2:("Venus",0.91), 3:("Mars",0.38),4:("Jupiter",2.53),5:("Saturn",1.07),6:("Uranus",0.89),7:("Neptune",1.14)}

weight=float(input("Enter your earth weight: "))
num=int(input("Enter planet number (1-7): "))
if num in planets:
    gravity=planets[num]
    planet_weight=weight*gravity
    print(f"Your weight on the planet is {planet_weight}")
else:
    print("Invalid planet number")