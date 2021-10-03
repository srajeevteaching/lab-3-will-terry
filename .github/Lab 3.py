# Programmers: [Terrence, Will, Hanna]
# Course: CS151, Dr. Rajeev
# Date: Lab Number: 3
# Program Inputs: [weight, distance]
# Program Outputs: [charge]

weight=float(input("please give weight in kg"))
distance=float(input("please give distance in miles"))

if weight >20 or weight <=0:
    print("your package either weighs too much or is a negative weight")
elif distance <10 or distance>3000:
    print("your distance is either too far or too close")
elif weight <=2:
    charge = (distance/500)*1.10
elif weight <=6:
    charge = (distance/500)*2.20
elif weight <=10:
    charge = (distance/500)*3.70
elif weight <=20:
    charge = (distance/500)*4.80

print("your charge is $%.2f dollars" %charge)