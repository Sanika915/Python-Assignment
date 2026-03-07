# Implement Simple Linear Regression manually without using any ML library.
# Dataset :
#     X = [1,2,3,4,5]
#     Y = [3,4,2,4,5]
# Tasks :
# Calculate:
#  1. Mean of X (X)
#  2. Mean of Y (Y)
#  3. Slope (m)
#  4. Intercept(c)

# Simple Linear Regression without ML library
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

n = len(X)

# Mean of X
mean_x = sum(X)/n

# Mean of Y
mean_y = sum(Y)/n

print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)

# Calculate slope (m)
num = 0
den = 0

for i in range(n):
    num += (X[i]-mean_x)*(Y[i]-mean_y)
    den += (X[i]-mean_x)**2

m = num/den

# Intercept (c)
c = mean_y - m*mean_x

print("Slope (m) =", round(m,2))
print("Intercept (c) =", round(c,2))

print("Regression Equation:")
print("Y =",round(m,2),"x +",round(c,2))

# Prediction for X = 6
x_new = 6
y_pred = m*x_new + c

print("Predicted Y for X = 6 :",round(y_pred,1))

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\Assi42>python Assi42Q1.py
# Mean of X = 3.0
# Mean of Y = 3.6
# Slope (m) = 0.4
# Intercept (c) = 2.4
# Regression Equation:
# Y = 0.4 x + 2.4
# Predicted Y for X = 6 : 4.8