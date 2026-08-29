import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

print("=" * 40)
print("DAY 19: TRAIN/TEST SPLIT & FEATURES")
print("=" * 40)

# ============================================================
# PART 1: CREATE A REALISTIC DATASET
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

# Marks roughly depend on study hours + attendance (with some randomness)
data["Marks"] = (
    data["StudyHours"] * 6
    + data["AttendancePercent"] * 0.3
    + np.random.randint(-5, 5, n_students)
)
data["Marks"] = np.clip(data["Marks"], 0, 100)  # keep marks realistic (0-100)

df = pd.DataFrame(data)
print(df.head(10))
print(f"\nTotal students: {len(df)}")


# ============================================================
# PART 2: SEPARATING FEATURES (X) AND LABEL (y)
# ============================================================

print("\n" + "=" * 40)
print("PART 2: FEATURES vs LABEL")
print("=" * 40)

# X = the INPUTS the model will use to predict
X = df[["StudyHours", "Age", "AttendancePercent"]]

# y = the ANSWER we want the model to learn to predict
y = df["Marks"]

print("Features (X) - first 5 rows:")
print(X.head())

print("\nLabel (y) - first 5 values:")
print(y.head())

print(f"\nX shape: {X.shape}")   # (50, 3) - 50 rows, 3 feature columns
print(f"y shape: {y.shape}")     # (50,)   - 50 values, 1 dimension


# ============================================================
# PART 3: SPLITTING INTO TRAIN AND TEST SETS
# ============================================================

print("\n" + "=" * 40)
print("PART 3: TRAIN/TEST SPLIT")
print("=" * 40)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% for testing, 80% for training
    random_state=42     # reproducible split
)

print(f"Training set size: {len(X_train)} students")
print(f"Testing set size: {len(X_test)} students")

print("\nTraining features preview:")
print(X_train.head())

print("\nTesting features preview:")
print(X_test.head())


# ============================================================
# PART 4: WHY THE SPLIT MATTERS - PROVING IT'S RANDOM
# ============================================================

print("\n" + "=" * 40)
print("PART 4: CONFIRMING RANDOM SPLIT")
print("=" * 40)

print("Indices in training set (first 10):")
print(list(X_train.index[:10]))

print("\nIndices in testing set (first 10):")
print(list(X_test.index[:10]))

print("\nNo overlap between train/test indices?",
      len(set(X_train.index) & set(X_test.index)) == 0)


# ============================================================
# PART 5: DIFFERENT SPLIT RATIOS
# ============================================================

print("\n" + "=" * 40)
print("PART 5: TRYING A DIFFERENT SPLIT RATIO")
print("=" * 40)

X_train70, X_test30, y_train70, y_test30 = train_test_split(
    X, y,
    test_size=0.3,   # 70/30 split instead of 80/20
    random_state=42
)

print(f"70/30 split -> Training: {len(X_train70)}, Testing: {len(X_test30)}")
print(f"80/20 split -> Training: {len(X_train)}, Testing: {len(X_test)}")


print("\n" + "=" * 40)
print("DAY 19 COMPLETED")
print("=" * 40)
print("\nNext up (Day 20): using X_train/y_train to actually TRAIN")
print("a Linear Regression model, then testing it on X_test/y_test!")
