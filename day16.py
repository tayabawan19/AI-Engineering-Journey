import pandas as pd


print("=" * 40)
print("DAY 16: PANDAS BASICS")
print("=" * 40)


# ============================================================
# PART 1: CREATING A SERIES
# ============================================================

print("\n" + "=" * 40)
print("PART 1: CREATING A SERIES")
print("=" * 40)

ages = pd.Series([20, 21, 22, 23, 24])

print("Ages:")
print(ages)

print("Type:", type(ages))
print("First age:", ages[0])
print("Last age:", ages.iloc[-1])


# ============================================================
# PART 2: CREATING A DATAFRAME
# ============================================================

print("\n" + "=" * 40)
print("PART 2: CREATING A DATAFRAME")
print("=" * 40)

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [85, 78, 92, 67, 88],
    "City": ["Islamabad", "Lahore", "Karachi", "Peshawar", "Islamabad"]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

print("\nType:", type(df))


# ============================================================
# PART 3: ACCESSING COLUMNS
# ============================================================

print("\n" + "=" * 40)
print("PART 3: ACCESSING COLUMNS")
print("=" * 40)

print("Names:")
print(df["Name"])

print("\nMarks:")
print(df["Marks"])

print("\nName and Marks:")
print(df[["Name", "Marks"]])


# ============================================================
# PART 4: INSPECTING THE DATA
# ============================================================

print("\n" + "=" * 40)
print("PART 4: INSPECTING THE DATA")
print("=" * 40)

print("First 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData information:")
df.info()

print("\nBasic statistics:")
print(df.describe())


# ============================================================
# PART 5: INDEXING & SELECTING ROWS
# ============================================================

print("\n" + "=" * 40)
print("PART 5: INDEXING & SELECTING ROWS")
print("=" * 40)

print("First row:")
print(df.iloc[0])

print("\nSecond row:")
print(df.iloc[1])

print("\nFirst three rows:")
print(df.iloc[0:3])

print("\nFirst row, Name:")
print(df.iloc[0]["Name"])


# ============================================================
# PART 6: FILTERING DATA
# ============================================================

print("\n" + "=" * 40)
print("PART 6: FILTERING DATA")
print("=" * 40)

print("Students with marks greater than 80:")
high_marks = df[df["Marks"] > 80]
print(high_marks)

print("\nStudents younger than 22:")
young_students = df[df["Age"] < 22]
print(young_students)

print("\nStudents from Islamabad:")
islamabad_students = df[df["City"] == "Islamabad"]
print(islamabad_students)


# ============================================================
# PART 7: MULTIPLE CONDITIONS
# ============================================================

print("\n" + "=" * 40)
print("PART 7: MULTIPLE CONDITIONS")
print("=" * 40)

print("Students older than 20 AND marks greater than 80:")

result = df[(df["Age"] > 20) & (df["Marks"] > 80)]

print(result)

print("\nStudents from Islamabad OR Lahore:")

result = df[
    (df["City"] == "Islamabad") |
    (df["City"] == "Lahore")
]

print(result)


# ============================================================
# PART 8: BASIC STATISTICS
# ============================================================

print("\n" + "=" * 40)
print("PART 8: BASIC STATISTICS")
print("=" * 40)

print("Average marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())
print("Total marks:", df["Marks"].sum())
print("Median marks:", df["Marks"].median())


# ============================================================
# PART 9: ADDING A NEW COLUMN
# ============================================================

print("\n" + "=" * 40)
print("PART 9: ADDING A NEW COLUMN")
print("=" * 40)

df["Passed"] = df["Marks"] >= 50

print("DataFrame after adding Passed column:")
print(df)


# ============================================================
# PART 10: CALCULATING AVERAGE
# ============================================================

print("\n" + "=" * 40)
print("PART 10: CALCULATING AVERAGE")
print("=" * 40)

df["Average"] = df["Marks"]

print("DataFrame with Average column:")
print(df)


# ============================================================
# PART 11: SORTING DATA
# ============================================================

print("\n" + "=" * 40)
print("PART 11: SORTING DATA")
print("=" * 40)

print("Students sorted by marks - highest first:")

sorted_df = df.sort_values("Marks", ascending=False)

print(sorted_df)


# ============================================================
# PART 12: REMOVING A COLUMN
# ============================================================

print("\n" + "=" * 40)
print("PART 12: REMOVING A COLUMN")
print("=" * 40)

df = df.drop("Average", axis=1)

print("DataFrame after removing Average:")
print(df)


# ============================================================
# PART 13: CREATING DATA FROM A CSV FILE
# ============================================================

print("\n" + "=" * 40)
print("PART 13: READING CSV FILE")
print("=" * 40)

# Create a CSV file named students.csv with:
#
# Name,Age,Marks,City
# Ali,21,85,Islamabad
# Ahmed,22,78,Lahore
# Sara,20,92,Karachi
# Usman,23,67,Peshawar
# Ayesha,21,88,Islamabad
#
# Then uncomment the following lines:

csv_df = pd.read_csv("students.csv")

print("Data loaded from CSV:")
print(csv_df)


# ============================================================
# PART 14: SAVING DATA TO CSV
# ============================================================

print("\n" + "=" * 40)
print("PART 14: SAVING DATA TO CSV")
print("=" * 40)

df.to_csv("students_output.csv", index=False)

print("Data successfully saved to students_output.csv")


# ============================================================
# PART 15: FINAL DATA ANALYSIS
# ============================================================

print("\n" + "=" * 40)
print("PART 15: FINAL DATA ANALYSIS")
print("=" * 40)

print("Complete DataFrame:")
print(df)

print("\nTotal students:", len(df))

print("Average class marks:", df["Marks"].mean())

print("Highest marks:", df["Marks"].max())

print("Lowest marks:", df["Marks"].min())

print("\nTop student:")

top_student = df.loc[df["Marks"].idxmax()]

print("Name:", top_student["Name"])
print("Marks:", top_student["Marks"])
print("City:", top_student["City"])


print("\n" + "=" * 40)
print("DAY 16 COMPLETED")
print("=" * 40)

