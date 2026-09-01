import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("=" * 40)
print("DAY 22: DECISION TREES & RANDOM FOREST")
print("=" * 40)

# ============================================================
# PART 1: RECREATE THE DATASET (same base as Day 19-21)
# ============================================================

print("\n" + "=" * 40)
print("PART 1: THE DATASET")
print("=" * 40)

np.random.seed(42)

n_students = 100
data = {
    "StudyHours": np.random.randint(1, 10, n_students),
    "Age": np.random.randint(18, 25, n_students),
    "AttendancePercent": np.random.randint(50, 100, n_students),
}

data["Marks"] = (
    data["StudyHours"] * 6
    + data["AttendancePercent"] * 0.3
    + np.random.randint(-5, 5, n_students)
)
data["Marks"] = np.clip(data["Marks"], 0, 100)

df = pd.DataFrame(data)
df["Passed"] = (df["Marks"] >= 50).astype(int)

print(df.head())


# ============================================================
# PART 2: FEATURES, LABEL, TRAIN/TEST SPLIT
# ============================================================

print("\n" + "=" * 40)
print("PART 2: SPLITTING THE DATA")
print("=" * 40)

X = df[["StudyHours", "Age", "AttendancePercent"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# ============================================================
# PART 3: DECISION TREE - TRAINING
# ============================================================

print("\n" + "=" * 40)
print("PART 3: DECISION TREE")
print("=" * 40)

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

tree_predictions = tree_model.predict(X_test)
tree_accuracy = accuracy_score(y_test, tree_predictions)

print(f"Decision Tree Accuracy: {tree_accuracy:.2%}")


# ============================================================
# PART 4: SEEING THE TREE'S DECISION RULES
# ============================================================

print("\n" + "=" * 40)
print("PART 4: THE TREE'S ACTUAL RULES")
print("=" * 40)

from sklearn.tree import export_text

rules = export_text(tree_model, feature_names=list(X.columns), max_depth=3)
print(rules)


# ============================================================
# PART 5: RANDOM FOREST - TRAINING
# ============================================================

print("\n" + "=" * 40)
print("PART 5: RANDOM FOREST")
print("=" * 40)

forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
forest_model.fit(X_train, y_train)

forest_predictions = forest_model.predict(X_test)
forest_accuracy = accuracy_score(y_test, forest_predictions)

print(f"Random Forest Accuracy: {forest_accuracy:.2%}")
print(f"(This forest is made of {forest_model.n_estimators} individual trees voting together)")


# ============================================================
# PART 6: COMPARING ALL 3 MODELS SO FAR
# ============================================================

print("\n" + "=" * 40)
print("PART 6: MODEL COMPARISON")
print("=" * 40)

from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
logistic_accuracy = accuracy_score(y_test, logistic_model.predict(X_test))

comparison = pd.DataFrame({
    "Model": ["Logistic Regression", "Decision Tree", "Random Forest"],
    "Accuracy": [logistic_accuracy, tree_accuracy, forest_accuracy]
})
comparison["Accuracy"] = comparison["Accuracy"].apply(lambda x: f"{x:.2%}")
print(comparison)


# ============================================================
# PART 7: FEATURE IMPORTANCE (Random Forest bonus)
# ============================================================

print("\n" + "=" * 40)
print("PART 7: WHICH FEATURES MATTER MOST?")
print("=" * 40)

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": forest_model.feature_importances_
}).sort_values("Importance", ascending=False)

print(importance_df)


# ============================================================
# PART 8: PREDICTING A NEW STUDENT WITH RANDOM FOREST
# ============================================================

print("\n" + "=" * 40)
print("PART 8: PREDICTING A NEW STUDENT")
print("=" * 40)

new_student = pd.DataFrame({
    "StudyHours": [6],
    "Age": [22],
    "AttendancePercent": [78]
})

prediction = forest_model.predict(new_student)[0]
probability = forest_model.predict_proba(new_student)[0]

result = "Pass" if prediction == 1 else "Fail"
print("New student profile:")
print(new_student)
print(f"\nRandom Forest Prediction: {result}")
print(f"Confidence: Fail={probability[0]:.2%}, Pass={probability[1]:.2%}")


print("\n" + "=" * 40)
print("DAY 22 COMPLETED")
print("=" * 40)
print("\nYou've now trained 3 different algorithms on the SAME data")
print("using the exact same workflow - that's the power of scikit-learn's")
print("consistent design pattern!")