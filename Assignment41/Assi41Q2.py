# The value of K plays an importnat role in the KNN algorithm.
# Write a Python program that demonstrates how prediction changes when K changes.
# Dataset.
# Use the same dataset as Assignment 1.
# Tasks:
# Predict the class of the same point using:
# K = 1
# K = 3
# K = 5
# Explain why the prediction changes when K increases

import math

# Dataset
data = [
    ('A',1,2,'Red'),
    ('B',2,3,'Red'),
    ('C',3,1,'Blue'),
    ('D',6,5,'Blue')
]

x = 2
y = 2

distances = []

for point,px,py,label in data:
    dist = math.sqrt((x-px)**2 + (y-py)**2)
    distances.append((point,dist,label))

distances.sort(key=lambda d: d[1])

def predict(k):
    neighbors = distances[:k]
    
    red = 0
    blue = 0
    
    for n in neighbors:
        if n[2] == "Red":
            red += 1
        else:
            blue += 1
            
    if red > blue:
        return "Red"
    else:
        return "Blue"

print("Prediction Results")

print("K = 1 ->",predict(1))
print("K = 3 ->",predict(3))
print("K = 5 ->",predict(5))

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\Assi41>python Assi41Q2.py
# Prediction Results
# K = 1 -> Red
# K = 3 -> Red
# K = 5 -> Blue