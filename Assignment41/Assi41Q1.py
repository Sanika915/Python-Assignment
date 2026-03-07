# Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
# The algorithm should be implemented manually without using any machine learning library.
# The program should:
# Calculate Euclidean distance.
# Sort distances
# Select k nearest neighbors
# Predict the class based on majority voting.
# Tasks:
# 1. Accept X and Y coordinates of a new point from the user.
# 2. Compute Euclidean distance from all dataset points.
# 3. Sort the distances.
# 4. Select K = 3 nearest neighbors.
# 5. Predict the class label.

import math

# Dataset
data = [
    ('A',1,2,'Red'),
    ('B',2,3,'Red'),
    ('C',3,1,'Blue'),
    ('D',6,5,'Blue')
]

# Accept input
x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

distances = []

# Calculate Euclidean distance
for point,px,py,label in data:
    dist = math.sqrt((x-px)**2 + (y-py)**2)
    distances.append((point,dist,label))

# Sort distances
distances.sort(key=lambda d: d[1])

# Select K = 3 neighbors
k = 3
neighbors = distances[:k]

print("\nNearest Neighbors:")

red = 0
blue = 0

for p,d,l in neighbors:
    print(p,"- Distance:",round(d,2))
    
    if l == "Red":
        red += 1
    else:
        blue += 1

# Majority voting
if red > blue:
    result = "Red"
else:
    result = "Blue"

print("\nPredicted Class:",result)

# Output is :
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\Assi41>python Assi41Q1.py
# Enter X coordinate: 2
# Enter Y coordinate: 2

# Nearest Neighbors:
# A - Distance: 1.0
# B - Distance: 1.0
# C - Distance: 1.41
# Predicted Class: Red