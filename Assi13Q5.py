# Write a program which accepts marks and display grade.

marks = int(input("Enter marks:"))

if marks >= 75:
    print("Distinction")

elif marks >= 60:
    print("First Class")

elif marks >= 50:
    print("Second Class")

else:
    print("Fail")   

# Output is:
# Enter marks:79
# Distinction     