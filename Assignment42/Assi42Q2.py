# Using the same dataset from above question, calculate model performance.
# Tasks:
# 1. Predict all Y values using regression equation.
# 2. calculate:
#    Mean squared Error(MSE)
#    R^2 Score
# Show all intermediate calculations.

# Model Performance Calculation
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

mean_x = sum(X)/len(X)
mean_y = sum(Y)/len(Y)

num = 0
den = 0

for i in range(len(X)):
    num += (X[i]-mean_x)*(Y[i]-mean_y)
    den += (X[i]-mean_x)**2

m = num/den
c = mean_y - m*mean_x

# Predict Y values
Y_pred = []

for x in X:
    Y_pred.append(m*x + c)

print("Predicted Y values:",Y_pred)

# MSE
error = 0

for i in range(len(Y)):
    error += (Y[i] - Y_pred[i])**2

mse = error/len(Y)

print("Mean Squared Error =",round(mse,2))

# R2 Score
ss_total = 0
ss_res = 0

for i in range(len(Y)):
    ss_total += (Y[i]-mean_y)**2
    ss_res += (Y[i]-Y_pred[i])**2

r2 = 1 - (ss_res/ss_total)

print("R2 Score =",round(r2,2))

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\Assi42>python Assi42Q2.py
# Predicted Y values: [2.8, 3.2, 3.6, 4.0, 4.4]
# Mean Squared Error = 0.72
# R2 Score = 0.31