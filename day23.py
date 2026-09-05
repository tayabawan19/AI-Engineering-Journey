import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

print("=" * 40)
print("DAY 23: MODEL EVALUATION METRICS")
print("=" * 40)

# ============================================================
# PART 1: CREATE AN IMBALANCED DATASET (to prove accuracy lies)
# ============================================================

print("\n" + "=" * 40)
print("PART 1: AN IMBALANCED DATASET")
print("=" * 40)

np.random.seed(42)

n_students = 200
data = {
    "StudyHours": np.random.randint(1, 10, n_students),
    "Age": np.random.randint(18, 25, n_students),
    "AttendancePercent": np.random.randint(30, 100, n_students),
}

data["Marks"] = (
    data["StudyHours"] * 5
    + data["AttendancePercent"] * 0.4
    + np.random.randint(-10, 10, n_students)
)
data["Marks"] = np.clip(data["Marks"], 0, 100)

df = pd.DataFrame(data)
df["Passed"] = (df["Marks"] >= 35).astype(int)

print(f"Pass count: {df['Passed'].sum()}")
print(f"Fail count: {len(df) - df['Passed'].sum()}")
print(f"Pass percentage: {df['Passed'].mean():.1%}  <- imbalanced!")


# ============================================================
# PART 2: TRAIN A MODEL
# ============================================================

print("\n" + "=" * 40)
print("PART 2: TRAINING A MODEL")
print("=" * 40)

X = df[["StudyHours", "Age", "AttendancePercent"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("✅ Model trained")


# ============================================================
# PART 3: THE PROBLEM WITH ACCURACY ALONE
# ============================================================

print("\n" + "=" * 40)
print("PART 3: WHY ACCURACY CAN LIE")
print("=" * 40)

accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.2%}")

lazy_predictions = np.ones(len(y_test))
lazy_accuracy = accuracy_score(y_test, lazy_predictions)
print(f"Lazy model (always predicts Pass) Accuracy: {lazy_accuracy:.2%}")
print("^ See how high this is even though it learned NOTHING? That's the trap.")


# ============================================================
# PART 4: THE CONFUSION MATRIX
# ============================================================

print("\n" + "=" * 40)
print("PART 4: CONFUSION MATRIX")
print("=" * 40)

cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(cm)

tn, fp, fn, tp = cm.ravel()
print(f"\nTrue Negatives (correctly predicted Fail): {tn}")
print(f"False Positives (predicted Pass, actually Fail): {fp}")
print(f"False Negatives (predicted Fail, actually Pass): {fn}")
print(f"True Positives (correctly predicted Pass): {tp}")


# ============================================================
# PART 5: PRECISION, RECALL, F1
# ============================================================

print("\n" + "=" * 40)
print("PART 5: PRECISION, RECALL, F1 SCORE")
print("=" * 40)

precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print(f"Precision: {precision:.2%}  (of predicted Pass, how many really passed)")
print(f"Recall:    {recall:.2%}  (of actual Pass students, how many did we catch)")
print(f"F1 Score:  {f1:.2%}  (balanced score combining both)")


# ============================================================
# PART 6: FULL CLASSIFICATION REPORT
# ============================================================

print("\n" + "=" * 40)
print("PART 6: FULL CLASSIFICATION REPORT")
print("=" * 40)

report = classification_report(y_test, predictions, target_names=["Fail", "Pass"])
print(report)


# ============================================================
# PART 7: A DELIBERATELY WEAK MODEL TO SEE METRICS DIFFER
# ============================================================

print("\n" + "=" * 40)
print("PART 7: COMPARING A WEAKER MODEL")
print("=" * 40)

weak_model = LogisticRegression(max_iter=1000)
weak_model.fit(X_train[:15], y_train[:15])
weak_predictions = weak_model.predict(X_test)

print("Weak model (trained on only 15 samples) report:")
print(classification_report(y_test, weak_predictions, target_names=["Fail", "Pass"]))

print("Strong model (trained on full data) report:")
print(classification_report(y_test, predictions, target_names=["Fail", "Pass"]))

print("\nNotice how accuracy might look similar, but precision/recall")
print("for the 'Fail' class often reveals the weak model struggling")
print("way more on the minority class!")


print("\n" + "=" * 40)
print("DAY 23 COMPLETED")
print("=" * 40)