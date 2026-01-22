# Write a program which accepts radius of circle and prints area of circle.

import math 

radius = float(input("Enter radius of the circle: "))

if radius <= 0:
    print("Invalid radius")
else:
    area = math.pi * radius ** 2
    print("Area of circle:", area)

# Output is:
# Enter radius of the circle: 4
# Area of circle: 50.26548245743669