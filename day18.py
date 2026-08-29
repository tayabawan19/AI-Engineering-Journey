import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 40)
print("DAY 18: DATA VISUALIZATION")
print("=" * 40)

# ============================================================
# SETUP: A REALISTIC STUDENT DATASET
# ============================================================

np.random.seed(42)  # makes random numbers reproducible - same result every run

data = {
    "Name": [f"Student{i}" for i in range(1, 31)],
    "Age": np.random.randint(18, 25, 30),
    "StudyHours": np.random.randint(1, 10, 30),
    "Marks": np.random.randint(40, 100, 30),
    "City": np.random.choice(["Islamabad", "Lahore", "Karachi", "Peshawar"], 30)
}

df = pd.DataFrame(data)
print("Dataset preview:")
print(df.head())


# ============================================================
# PART 1: LINE CHART
# ============================================================

print("\nGenerating Line Chart...")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
avg_marks_trend = [65, 68, 70, 72, 75, 78]

plt.figure(figsize=(8, 5))
plt.plot(months, avg_marks_trend, marker="o", color="green")
plt.title("Average Marks Trend Over 6 Months")
plt.xlabel("Month")
plt.ylabel("Average Marks")
plt.grid(True)
plt.savefig("chart1_line.png")
plt.show()


# ============================================================
# PART 2: BAR CHART
# ============================================================

print("Generating Bar Chart...")

city_avg = df.groupby("City")["Marks"].mean()

plt.figure(figsize=(8, 5))
city_avg.plot(kind="bar", color="skyblue")
plt.title("Average Marks by City")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.savefig("chart2_bar.png")
plt.show()


# ============================================================
# PART 3: HISTOGRAM
# ============================================================

print("Generating Histogram...")

plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=10, color="orange", edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("chart3_histogram.png")
plt.show()


# ============================================================
# PART 4: SCATTER PLOT
# ============================================================

print("Generating Scatter Plot...")

plt.figure(figsize=(8, 5))
plt.scatter(df["StudyHours"], df["Marks"], color="purple")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Marks")
plt.savefig("chart4_scatter.png")
plt.show()


# ============================================================
# PART 5: BOX PLOT (spotting outliers)
# ============================================================

print("Generating Box Plot...")

plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Marks"])
plt.title("Marks Distribution & Outliers")
plt.savefig("chart5_boxplot.png")
plt.show()


# ============================================================
# PART 6: HEATMAP (correlation between numeric columns)
# ============================================================

print("Generating Heatmap...")

numeric_df = df[["Age", "StudyHours", "Marks"]]
correlation = numeric_df.corr()

print("\nCorrelation matrix:")
print(correlation)

plt.figure(figsize=(6, 5))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("chart6_heatmap.png")
plt.show()


print("\n" + "=" * 40)
print("DAY 18 COMPLETED - 6 charts saved as PNG files")
print("=" * 40)