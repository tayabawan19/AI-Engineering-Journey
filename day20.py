import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

print("=" * 40)
print("DAY 20: LINEAR REGRESSION")
print("=" * 40)

# ============================================================
# PART 1: RECREATE THE DATASET (same as Day 19)
# ============================================================

print("\n" + "=" * 40)
print("PART 1: THE DATASET")
print("=" * 40)

np.random.seed(42)

n_students = 50
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
print(df.head())


# ============================================================
# PART 2: FEATURES, LABEL, TRAIN/TEST SPLIT (same as Day 19)
# ============================================================

print("\n" + "=" * 40)
print("PART 2: SPLITTING THE DATA")
print("=" * 40)

X = df[["StudyHours", "Age", "AttendancePercent"]]
y = df["Marks"]

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

model = LinearRegression()       # 1. Create the model
model.fit(X_train, y_train)      # 2. Train it on the training data

print("✅ Model trained!")

# The weights the model learned for each feature
print("\nLearned weights (coefficients):")
for feature, weight in zip(X.columns, model.coef_):
    print(f"  {feature}: {weight:.3f}")

print(f"\nIntercept (b): {model.intercept_:.3f}")


# ============================================================
# PART 4: MAKING PREDICTIONS
# ============================================================

print("\n" + "=" * 40)
print("PART 4: MAKING PREDICTIONS")
print("=" * 40)

predictions = model.predict(X_test)   # 3. Predict on unseen test data

# compare predicted vs actual side by side
comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions.round(1)
})
print(comparison)


# ============================================================
# PART 5: EVALUATING THE MODEL
# ============================================================

print("\n" + "=" * 40)
print("PART 5: HOW GOOD IS THE MODEL?")
print("=" * 40)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print(f"R² Score: {r2:.3f}")
print(f"  (1.0 = perfect, 0.0 = no better than guessing average)")

print(f"\nMean Absolute Error: {mae:.2f} marks")
print(f"  (On average, predictions are off by about {mae:.1f} marks)")


# ============================================================
# PART 6: PREDICTING FOR A NEW, UNSEEN STUDENT
# ============================================================

print("\n" + "=" * 40)
print("PART 6: PREDICTING A NEW STUDENT")
print("=" * 40)

# A brand new student the model has never seen before
new_student = pd.DataFrame({
    "StudyHours": [7],
    "Age": [21],
    "AttendancePercent": [85]
})

predicted_marks = model.predict(new_student)
print("New student profile:")
print(new_student)
print(f"\nPredicted Marks: {predicted_marks[0]:.1f}")


print("\n" + "=" * 40)
print("DAY 20 COMPLETED")
print("=" * 40)
print("\nYou just trained your FIRST real machine learning model!")
print("It learned patterns from 40 students and can now predict")
print("marks for students it has never seen before.")