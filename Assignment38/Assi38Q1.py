# Write a Python program to load the file student_performance_ml.csv using pandas.
# Display:
# First 5 records
# Last 5 records
# Total number of rows and columns
# List of column names
# Data types of each column

# ------------------------------------------------------------
# Student Performance ML - Complete Assignment (All 10 Tasks)
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv("student_performance_ml.csv")

print("\n================ QUESTION 1 ================")
print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nTotal Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# ------------------------------------------------------------
# 2. Total Students, Passed, Failed
# ------------------------------------------------------------

print("\n================ QUESTION 2 ================")

total_students = df.shape[0]
passed_students = df[df["FinalResult"] == 1].shape[0]
failed_students = df[df["FinalResult"] == 0].shape[0]

print("Total Students in Dataset:", total_students)
print("Number of Passed Students (FinalResult=1):", passed_students)
print("Number of Failed Students (FinalResult=0):", failed_students)

# ------------------------------------------------------------
# 3. Pandas Calculations
# ------------------------------------------------------------

print("\n================ QUESTION 3 ================")

print("Average StudyHours:", df["StudyHours"].mean())
print("Average Attendance:", df["Attendance"].mean())
print("Maximum PreviousScore:", df["PreviousScore"].max())
print("Minimum SleepHours:", df["SleepHours"].min())

# ------------------------------------------------------------
# 4. value_counts and Percentage
# ------------------------------------------------------------

print("\n================ QUESTION 4 ================")

result_counts = df["FinalResult"].value_counts()
print("\nDistribution of FinalResult:")
print(result_counts)

percentage = df["FinalResult"].value_counts(normalize=True) * 100
print("\nPercentage of Pass and Fail:")
print(percentage)

if abs(percentage[1] - percentage[0]) < 10:
    print("\nDataset is Balanced because Pass and Fail percentages are nearly equal.")
else:
    print("\nDataset is NOT Balanced because Pass and Fail percentages differ significantly.")

# ------------------------------------------------------------
# 5. Analysis Based on Dataset
# ------------------------------------------------------------

print("\n================ QUESTION 5 ================")

print("Observations:")
print("1. Students with higher StudyHours generally have higher chances of passing.")
print("2. Higher Attendance improves FinalResult.")
print("3. Students with good PreviousScore mostly pass.")
print("4. Completing more assignments increases probability of success.")

# ------------------------------------------------------------
# 6. Histogram of StudyHours
# ------------------------------------------------------------

print("\n================ QUESTION 6 ================")
print("Histogram shows distribution of StudyHours among students.")

plt.figure()
plt.hist(df["StudyHours"], bins=10)
plt.title("Histogram of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------------------------------
# 7. Scatter Plot: StudyHours vs PreviousScore
# ------------------------------------------------------------

print("\n================ QUESTION 7 ================")
print("Scatter plot shows relationship between StudyHours and PreviousScore.")

plt.figure()

pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

plt.scatter(pass_students["StudyHours"], pass_students["PreviousScore"], label="Pass")
plt.scatter(fail_students["StudyHours"], fail_students["PreviousScore"], label="Fail")

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.show()

# ------------------------------------------------------------
# 8. Boxplot for Attendance
# ------------------------------------------------------------

print("\n================ QUESTION 8 ================")
print("Boxplot identifies spread and possible outliers in Attendance.")

plt.figure()
plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")
plt.show()

# ------------------------------------------------------------
# 9. AssignmentsCompleted vs FinalResult
# ------------------------------------------------------------

print("\n================ QUESTION 9 ================")
print("Relationship between AssignmentsCompleted and FinalResult.")

plt.figure()
plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")
plt.title("AssignmentsCompleted vs FinalResult")
plt.show()

# ------------------------------------------------------------
# 10. SleepHours vs FinalResult
# ------------------------------------------------------------

print("\n================ QUESTION 10 ================")
print("SleepHours vs FinalResult Analysis")

plt.figure()
plt.scatter(df["SleepHours"], df["FinalResult"])
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.title("SleepHours vs FinalResult")
plt.show()

print("Conclusion: Sleeping more does not guarantee success.")
print("Balanced sleep along with study and attendance is important.")

print("\n================ END OF ASSIGNMENT ================")