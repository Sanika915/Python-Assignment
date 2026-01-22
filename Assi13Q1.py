# Write a program which accepts length and width of rectangle and prints area.

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

if length <= 0 or width <= 0:
    print("Invalid dimensions")
else:
    area = length * width
    print("Area of rectangle:", area)

# Output is:
# Enter length of rectangle: 5.6
# Enter width of rectangle: 7.5
# Area of rectangle: 42.0