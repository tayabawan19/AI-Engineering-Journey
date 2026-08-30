import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("=" * 40)
print("DAY 21: CLASSIFICATION (LOGISTIC REGRESSION)")
print("=" * 40)

# ============================================================
# PART 1: RECREATE THE DATASET (same base as Day 19/20)
# ============================================================

print("\n" + "=" * 40)
print("PART 1: THE DATASET")
print("=" * 40)

np.random.seed(42)

n_students = 100  # more students this time for a more reliable model
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

# ===== NEW: create the CATEGORY we want to predict =====
df["Passed"] = (df["Marks"] >= 50).astype(int)  # 1 = Pass, 0 = Fail

print(df.head(10))
print(f"\nPass count: {df['Passed'].sum()}")
print(f"Fail count: {len(df) - df['Passed'].sum()}")


# ============================================================
# PART 2: FEATURES, LABEL, TRAIN/TEST SPLIT
# ============================================================

print("\n" + "=" * 40)
print("PART 2: SPLITTING THE DATA")
print("=" * 40)

X = df[["StudyHours", "Age", "AttendancePercent"]]
y = df["Passed"]   # this time our label is a CATEGORY (0 or 1), not a number

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# ============================================================
# PART 3: CREATE AND TRAIN THE MODEL
# ============================================================

print("\n" + "=" * 40)
print("PART 3: TRAINING THE MODEL")
print("=" * 40)

model = LogisticRegression()
model.fit(X_train, y_train)

print("✅ Model trained!")


# ============================================================
# PART 4: MAKING PREDICTIONS
# ============================================================

print("\n" + "=" * 40)
print("PART 4: MAKING PREDICTIONS")
print("=" * 40)

predictions = model.predict(X_test)

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})
comparison["Actual"] = comparison["Actual"].map({1: "Pass", 0: "Fail"})
comparison["Predicted"] = comparison["Predicted"].map({1: "Pass", 0: "Fail"})
print(comparison)


# ============================================================
# PART 5: LOOKING AT PROBABILITIES (not just the final answer)
# ============================================================

print("\n" + "=" * 40)
print("PART 5: PREDICTION PROBABILITIES")
print("=" * 40)

# predict_proba gives the probability of each class, not just the final label
probabilities = model.predict_proba(X_test)

print("First 5 students - [Probability of Fail, Probability of Pass]:")
for i in range(5):
    fail_prob, pass_prob = probabilities[i]
    print(f"  Student {i+1}: Fail={fail_prob:.2f}, Pass={pass_prob:.2f}")


# ============================================================
# PART 6: EVALUATING THE MODEL
# ============================================================

print("\n" + "=" * 40)
print("PART 6: HOW ACCURATE IS THE MODEL?")
print("=" * 40)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")
print(f"({int(accuracy * len(y_test))} out of {len(y_test)} predictions correct)")


# ============================================================
# PART 7: PREDICTING FOR A NEW STUDENT
# ============================================================

print("\n" + "=" * 40)
print("PART 7: PREDICTING A NEW STUDENT")
print("=" * 40)

new_student = pd.DataFrame({
    "StudyHours": [2],
    "Age": [20],
    "AttendancePercent": [55]
})

prediction = model.predict(new_student)[0]
probability = model.predict_proba(new_student)[0]

result = "Pass" if prediction == 1 else "Fail"
print("New student profile (low study hours, low attendance):")
print(new_student)
print(f"\nPrediction: {result}")
print(f"Confidence: Fail={probability[0]:.2%}, Pass={probability[1]:.2%}")


print("\n" + "=" * 40)
print("DAY 21 COMPLETED")
print("=" * 40)
print("\nYou trained a CLASSIFICATION model - it now predicts")
print("categories (Pass/Fail) instead of exact numbers!")