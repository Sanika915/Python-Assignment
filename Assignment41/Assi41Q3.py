# Use KNN to predict whether a student passes or fails based on study hours and attendance.
# Dataset:
# Tasks:
# 1. Accept input from user:
#    Study hours
#    Attendance percentage
# 2. Apply KNN algorithm
# 3. Predict whether the student Passes or Fails.

import math

# Dataset
data = [
    (2,60,'Fail'),
    (5,80,'Pass'),
    (6,85,'Pass'),
    (1,50,'Fail')
]

# User input
study = int(input("Enter Study Hours: "))
attendance = int(input("Enter Attendance: "))

distances = []

# Distance calculation
for s,a,label in data:
    dist = math.sqrt((study-s)**2 + (attendance-a)**2)
    distances.append((dist,label))

# Sort
distances.sort()

# K = 3
k = 3
neighbors = distances[:k]

pass_count = 0
fail_count = 0

for d,l in neighbors:
    if l == "Pass":
        pass_count += 1
    else:
        fail_count += 1

# Prediction
if pass_count > fail_count:
    result = "Pass"
else:
    result = "Fail"

print("\nPredicted Result:",result)

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\Assi41>python Assi41Q3.py
# Enter Study Hours: 4
# Enter Attendance: 70
# Predicted Result: Pass