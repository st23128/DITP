height1 = float(input("Enter height of student 1 in cm: "))
weight1 = float(input("Enter weight of student 1 in kg: "))
height2 = float(input("Enter height of student 2 in cm: "))
weight2 = float(input("Enter weight of student 2 in kg: "))
height3 = float(input("Enter height of student 3 in cm: "))
weight3 = float(input("Enter weight of student 3 in kg: "))

average_weight = (weight1 + weight2 + weight3)/3
average_height = (height1 + height2 + height3)/3

print("The average weight is: {:.2f} kg".format(average_weight))
print("The average height is: {:.2f} cm".format(average_height))
