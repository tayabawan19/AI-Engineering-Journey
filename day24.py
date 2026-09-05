"""
Day 24 — Overfitting & Underfitting
Using a Decision Tree on a synthetic classification dataset to visually
demonstrate the overfitting/underfitting tradeoff as tree depth increases.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Create a synthetic dataset (like Day 22's setup, but reusable/reproducible)
X, y = make_classification(
    n_samples=500,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    random_state=42
)

# 2. Split into train/test (Day 19 concept)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. Train Decision Trees at increasing depths, track train vs test accuracy
depths = range(1, 21)
train_scores = []
test_scores = []

for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_acc = accuracy_score(y_train, train_pred)
    test_acc = accuracy_score(y_test, test_pred)

    train_scores.append(train_acc)
    test_scores.append(test_acc)

    print(f"Depth {depth:2d} | Train Acc: {train_acc:.3f} | Test Acc: {test_acc:.3f}")

# 4. Also check the "no limit" case — classic overfitting setup
unlimited_model = DecisionTreeClassifier(random_state=42)  # no max_depth
unlimited_model.fit(X_train, y_train)
unlimited_train_acc = accuracy_score(y_train, unlimited_model.predict(X_train))
unlimited_test_acc = accuracy_score(y_test, unlimited_model.predict(X_test))
print(f"\nNo depth limit | Train Acc: {unlimited_train_acc:.3f} | Test Acc: {unlimited_test_acc:.3f}")

# 5. Plot train vs test accuracy across depths
plt.figure(figsize=(9, 6))
plt.plot(depths, train_scores, marker='o', label='Train Accuracy')
plt.plot(depths, test_scores, marker='o', label='Test Accuracy')
plt.axhline(y=max(test_scores), color='gray', linestyle='--', alpha=0.5, label='Best Test Accuracy')
plt.xlabel('Tree Depth (Model Complexity)')
plt.ylabel('Accuracy')
plt.title('Overfitting vs Underfitting — Decision Tree Depth Sweep')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(list(depths))
plt.tight_layout()
plt.savefig('day24_overfitting_plot.png', dpi=150)
plt.show()

print("\nPlot saved as day24_overfitting_plot.png")
print("\nWhat to look for:")
print("- Early depths (1-3): both train & test accuracy low -> underfitting")
print("- Middle depths: both accuracies rise together, close to each other -> good fit")
print("- Deep depths (10+): train accuracy keeps climbing toward 1.0,")
print("  but test accuracy plateaus or drops -> overfitting")