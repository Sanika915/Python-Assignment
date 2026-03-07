# Consider below task
# 1. Train linear regression model.
# 2. Predict salary for 6 years of experience.
# 3. Plot regression line using matplotlib.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([1,2,3,4,5]).reshape(-1,1)
Y = np.array([20000,25000,30000,35000,40000])

# Train model
model = LinearRegression()
model.fit(X,Y)

# Prediction
predicted_salary = model.predict([[6]])

print("Predicted Salary for 6 Years Experience: ₹", int(predicted_salary[0]))

# Plot graph
plt.scatter(X,Y,color='blue',label="Data points")

plt.plot(X,model.predict(X),color='red',label="Regression Line")

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction")

plt.legend()

plt.show()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\Assi42>python Assi42Q3.py
# Predicted Salary for 6 Years Experience: ₹ 45000