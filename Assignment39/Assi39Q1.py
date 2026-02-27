# ============================================================
# Student Performance ML - Complete Machine Learning Program
# ============================================================

# -------------------------
# 1. Import Libraries
# -------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# -------------------------
# 2. Load Dataset
# -------------------------

df = pd.read_csv("student_performance_ml.csv")

print("\n=========== DATASET INFORMATION ===========")
print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nShape (Rows, Columns):", df.shape)
print("\nColumns:", df.columns)
print("\nData Types:\n", df.dtypes)

# -------------------------
# 3. Basic Analysis
# -------------------------

print("\n=========== BASIC ANALYSIS ===========")

print("Total Students:", df.shape[0])
print("Passed Students:", df[df["FinalResult"] == 1].shape[0])
print("Failed Students:", df[df["FinalResult"] == 0].shape[0])

print("\nAverage StudyHours:", df["StudyHours"].mean())
print("Average Attendance:", df["Attendance"].mean())
print("Maximum PreviousScore:", df["PreviousScore"].max())
print("Minimum SleepHours:", df["SleepHours"].min())

print("\nFinalResult Distribution:")
print(df["FinalResult"].value_counts())

print("\nPercentage Distribution:")
print(df["FinalResult"].value_counts(normalize=True) * 100)

# -------------------------
# 4. Visualization
# -------------------------

print("\n=========== VISUALIZATION ===========")

# Histogram
plt.figure()
plt.hist(df["StudyHours"], bins=10)
plt.title("Histogram of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(df["StudyHours"], df["PreviousScore"])
plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.show()

# Boxplot
plt.figure()
plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.show()

# -------------------------
# 5. Prepare Data for ML
# -------------------------

print("\n=========== TRAIN TEST SPLIT ===========")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training Size:", X_train.shape)
print("Testing Size:", X_test.shape)

# -------------------------
# 6. Train Decision Tree Model
# -------------------------

print("\n=========== MODEL TRAINING ===========")

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# -------------------------
# 7. Prediction
# -------------------------

y_pred = model.predict(X_test)

print("\nPredicted Values:\n", y_pred)
print("\nActual Values:\n", y_test.values)

# -------------------------
# 8. Accuracy Calculation
# -------------------------

accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy: {:.2f}%".format(accuracy * 100))

# -------------------------
# 9. Confusion Matrix
# -------------------------

print("\n=========== CONFUSION MATRIX ===========")

cm = confusion_matrix(y_test, y_pred)
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

print("\nTrue Positive, True Negative, False Positive, False Negative explained from matrix above.")

# -------------------------
# 10. Training vs Testing Accuracy
# -------------------------

train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, y_pred)

print("\nTraining Accuracy: {:.2f}%".format(train_acc * 100))
print("Testing Accuracy: {:.2f}%".format(test_acc * 100))

if train_acc > test_acc:
    print("Model may be overfitting.")
else:
    print("Model is generalizing well.")

# -------------------------
# 11. Train 3 Models with Different Depth
# -------------------------

print("\n=========== COMPARING DIFFERENT MAX_DEPTH ===========")

depth1 = DecisionTreeClassifier(max_depth=1)
depth3 = DecisionTreeClassifier(max_depth=3)
depthNone = DecisionTreeClassifier(max_depth=None)

depth1.fit(X_train, y_train)
depth3.fit(X_train, y_train)
depthNone.fit(X_train, y_train)

print("Accuracy (max_depth=1): {:.2f}%".format(
    accuracy_score(y_test, depth1.predict(X_test)) * 100))

print("Accuracy (max_depth=3): {:.2f}%".format(
    accuracy_score(y_test, depth3.predict(X_test)) * 100))

print("Accuracy (max_depth=None): {:.2f}%".format(
    accuracy_score(y_test, depthNone.predict(X_test)) * 100))

# -------------------------
# 12. Predict for New Student
# -------------------------

print("\n=========== NEW STUDENT PREDICTION ===========")

new_student = [[6, 85, 66, 7, 7]]  # StudyHours, Attendance, PreviousScore, AssignmentsCompleted, SleepHours

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("The student will PASS.")
else:
    print("The student will FAIL.")

# -------------------------
# Final Conclusion
# -------------------------

print("\n=========== FINAL CONCLUSION ===========")
print("Decision Tree model successfully trained.")
print("Accuracy calculated.")
print("Confusion matrix generated.")
print("Overfitting checked.")
print("New student prediction completed.")