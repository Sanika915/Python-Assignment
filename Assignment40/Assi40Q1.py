# ============================================================
# ADVANCED MACHINE LEARNING TASKS
# ============================================================

print("\n================= 1. FEATURE IMPORTANCE =================")

# Feature Importance
importances = model.feature_importances_

for name, score in zip(X.columns, importances):
    print(f"{name} : {score:.4f}")

most_important = X.columns[importances.argmax()]
least_important = X.columns[importances.argmin()]

print("\nMost Important Feature:", most_important)
print("Least Important Feature:", least_important)


# ============================================================
# 2. Remove SleepHours and Retrain
# ============================================================

print("\n================= 2. REMOVE SleepHours =================")

X_removed = df.drop(["FinalResult", "SleepHours"], axis=1)
y_removed = df["FinalResult"]

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_removed, y_removed, test_size=0.3, random_state=42
)

model_removed = DecisionTreeClassifier()
model_removed.fit(X_train_r, y_train_r)

acc_removed = accuracy_score(y_test_r, model_removed.predict(X_test_r))
print("New Accuracy without SleepHours: {:.2f}%".format(acc_removed * 100))


# ============================================================
# 3. Train Using Only StudyHours & Attendance
# ============================================================

print("\n================= 3. LIMITED FEATURES =================")

X_limited = df[["StudyHours", "Attendance"]]
y_limited = df["FinalResult"]

X_train_l, X_test_l, y_train_l, y_test_l = train_test_split(
    X_limited, y_limited, test_size=0.3, random_state=42
)

model_limited = DecisionTreeClassifier()
model_limited.fit(X_train_l, y_train_l)

acc_limited = accuracy_score(y_test_l, model_limited.predict(X_test_l))
print("Accuracy with only StudyHours & Attendance: {:.2f}%".format(acc_limited * 100))


# ============================================================
# 4. Predict 5 New Students
# ============================================================

print("\n================= 4. 5 NEW STUDENTS =================")

new_students = pd.DataFrame([
    [5, 80, 70, 6, 7],
    [2, 60, 50, 3, 6],
    [7, 90, 88, 9, 8],
    [4, 75, 65, 5, 7],
    [6, 85, 78, 8, 6]
], columns=X.columns)

predictions = model.predict(new_students)

new_students["Prediction"] = predictions
print(new_students)


# ============================================================
# 5. Manual Accuracy Calculation
# ============================================================

print("\n================= 5. MANUAL ACCURACY =================")

correct = sum(y_test.values == y_pred)
manual_accuracy = correct / len(y_test)

print("Manual Accuracy: {:.2f}%".format(manual_accuracy * 100))
print("Sklearn Accuracy: {:.2f}%".format(accuracy * 100))


# ============================================================
# 6. Misclassified Students
# ============================================================

print("\n================= 6. MISCLASSIFIED =================")

misclassified = X_test[y_test != y_pred]
print(misclassified)

print("Total Misclassified:", misclassified.shape[0])


# ============================================================
# 7. Compare Different random_state
# ============================================================

print("\n================= 7. RANDOM STATE TEST =================")

for rs in [0, 10, 42]:
    X_train_rs, X_test_rs, y_train_rs, y_test_rs = train_test_split(
        X, y, test_size=0.3, random_state=rs
    )
    model_rs = DecisionTreeClassifier()
    model_rs.fit(X_train_rs, y_train_rs)
    acc_rs = accuracy_score(y_test_rs, model_rs.predict(X_test_rs))
    print(f"Accuracy with random_state={rs}: {acc_rs*100:.2f}%")


# ============================================================
# 8. Decision Tree Visualization
# ============================================================

print("\n================= 8. TREE VISUALIZATION =================")

from sklearn.tree import plot_tree

plt.figure(figsize=(12,6))
plot_tree(model, feature_names=X.columns, class_names=["Fail","Pass"], filled=True)
plt.show()

print("Root node feature generally is the most important feature.")


# ============================================================
# 9. Create PerformanceIndex Feature
# ============================================================

print("\n================= 9. PERFORMANCE INDEX =================")

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X_new = df.drop("FinalResult", axis=1)
y_new = df["FinalResult"]

X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(
    X_new, y_new, test_size=0.3, random_state=42
)

model_new = DecisionTreeClassifier()
model_new.fit(X_train_new, y_train_new)

acc_new = accuracy_score(y_test_new, model_new.predict(X_test_new))
print("Accuracy with PerformanceIndex: {:.2f}%".format(acc_new * 100))


# ============================================================
# 10. max_depth=None Training vs Testing
# ============================================================

print("\n================= 10. MAX_DEPTH NONE =================")

deep_model = DecisionTreeClassifier(max_depth=None)
deep_model.fit(X_train, y_train)

train_deep = accuracy_score(y_train, deep_model.predict(X_train))
test_deep = accuracy_score(y_test, deep_model.predict(X_test))

print("Training Accuracy:", train_deep * 100)
print("Testing Accuracy:", test_deep * 100)

if train_deep == 1.0 and test_deep < train_deep:
    print("Model is overfitting because it memorized training data.")