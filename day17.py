import pandas as pd
import numpy as np

print("=" * 40)
print("DAY 17: DATA CLEANING")
print("=" * 40)

# ============================================================
# PART 1: CREATE A MESSY DATASET (simulating real-world data)
# ============================================================

print("\n" + "=" * 40)
print("PART 1: THE MESSY DATASET")
print("=" * 40)

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha", "Ahmed", None],
    "Age": [21, 22, np.nan, 23, 21, 22, 25],
    "Marks": [85, 78, 92, np.nan, 88, 78, 200],  # 200 is an outlier/typo
    "City": ["Islamabad", "lahore", "Karachi ", "Peshawar", "islamabad", "lahore", "Lahore"]
}

df = pd.DataFrame(data)
print("Raw messy data:")
print(df)


# ============================================================
# PART 2: FINDING MISSING VALUES
# ============================================================

print("\n" + "=" * 40)
print("PART 2: FINDING MISSING VALUES")
print("=" * 40)

print("Missing values per cell (True = missing):")
print(df.isnull())

print("\nMissing values count PER COLUMN:")
print(df.isnull().sum())


# ============================================================
# PART 3: HANDLING MISSING VALUES
# ============================================================

print("\n" + "=" * 40)
print("PART 3: HANDLING MISSING VALUES")
print("=" * 40)

# Strategy A - fill missing Age with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("After filling missing Age with average:")
print(df)

# Strategy B - fill missing Marks with 0 (assume they didn't submit)
df["Marks"] = df["Marks"].fillna(0)
print("\nAfter filling missing Marks with 0:")
print(df)

# Strategy C - fill missing Name with "Unknown"
df["Name"] = df["Name"].fillna("Unknown")
print("\nAfter filling missing Name with 'Unknown':")
print(df)


# ============================================================
# PART 4: FINDING & REMOVING DUPLICATES
# ============================================================

print("\n" + "=" * 40)
print("PART 4: DUPLICATES")
print("=" * 40)

print("Which rows are duplicates?")
print(df.duplicated())

df_no_duplicates = df.drop_duplicates()
print("\nAfter removing duplicates:")
print(df_no_duplicates)


# ============================================================
# PART 5: FIXING INCONSISTENT TEXT
# ============================================================

print("\n" + "=" * 40)
print("PART 5: FIXING TEXT FORMATTING")
print("=" * 40)

print("Before cleaning City column:")
print(df["City"].unique())  # shows all UNIQUE values - reveals the mess

df["City"] = df["City"].str.strip()   # remove extra spaces
df["City"] = df["City"].str.lower()   # make everything lowercase
df["City"] = df["City"].str.capitalize()  # then capitalize nicely

print("\nAfter cleaning City column:")
print(df["City"].unique())
print(df)


# ============================================================
# PART 6: HANDLING OUTLIERS
# ============================================================

print("\n" + "=" * 40)
print("PART 6: HANDLING OUTLIERS")
print("=" * 40)

print("Marks before fixing outlier:")
print(df["Marks"])

# Marks should realistically be between 0-100
# Anything above 100 is clearly a data entry error
df.loc[df["Marks"] > 100, "Marks"] = df["Marks"].median()

print("\nMarks after capping outliers to the median:")
print(df["Marks"])


# ============================================================
# PART 7: FIXING DATA TYPES
# ============================================================

print("\n" + "=" * 40)
print("PART 7: FIXING DATA TYPES")
print("=" * 40)

print("Data types before:")
print(df.dtypes)

df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(int)

print("\nData types after:")
print(df.dtypes)


# ============================================================
# PART 8: FINAL CLEAN DATASET
# ============================================================

print("\n" + "=" * 40)
print("PART 8: FINAL CLEAN DATASET")
print("=" * 40)

df_clean = df.drop_duplicates().reset_index(drop=True)
print(df_clean)

print("\n✅ Cleaning summary:")
print(f"- Filled missing Age with average")
print(f"- Filled missing Marks with 0")
print(f"- Filled missing Name with 'Unknown'")
print(f"- Removed duplicate rows")
print(f"- Standardized City text formatting")
print(f"- Fixed outlier in Marks (capped at median)")
print(f"- Converted Age and Marks to proper integer type")

print("\n" + "=" * 40)
print("DAY 17 COMPLETED")
print("=" * 40)