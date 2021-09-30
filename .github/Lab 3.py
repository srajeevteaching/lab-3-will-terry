weight_of_package = float(input("weight_of_package"))
float(input("distance of shipping"))
maxWeight = 20
minWeight = 0
minDistance = 10
maxDistance = 3000
if weight_of_package <= minWeight or maxWeight < weight_of_package:
    print("sorry, cannot ship package")

if minDistance < 10 or maxDistance >3000:
    print