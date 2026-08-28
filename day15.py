import numpy as np

print("=" * 40)
print("PART 1: CREATING ARRAYS")
print("=" * 40)

arr = np.array([1, 2, 3, 4, 5])
print("Basic array:", arr)
print("Type:", type(arr))

zeros = np.zeros(5)
ones = np.ones(5)
print("Zeros:", zeros)
print("Ones:", ones)

range_arr = np.arange(0, 10, 2)  # start, stop, step
print("Range array:", range_arr)


# ===== 2. ARRAY SHAPES =====
print("\n" + "=" * 40)
print("PART 2: SHAPES (1D vs 2D)")
print("=" * 40)

arr_1d = np.array([1, 2, 3, 4])
print("1D array:", arr_1d)
print("Shape:", arr_1d.shape)  # (4,) = 4 elements, one dimension

arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n2D array:\n", arr_2d)
print("Shape:", arr_2d.shape)  # (2, 3) = 2 rows, 3 columns


# ===== 3. INDEXING & SLICING =====
print("\n" + "=" * 40)
print("PART 3: INDEXING & SLICING")
print("=" * 40)

arr = np.array([10, 20, 30, 40, 50])
print("Full array:", arr)
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice [1:4]:", arr[1:4])

grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("\nGrid:\n", grid)
print("Row 0:", grid[0])
print("Element at row 1, col 2:", grid[1, 2])
print("Entire column 0:", grid[:, 0])


# ===== 4. VECTORIZED MATH (NO LOOPS!) =====
print("\n" + "=" * 40)
print("PART 4: VECTORIZED MATH")
print("=" * 40)

numbers = np.array([1, 2, 3, 4, 5])
print("Original:", numbers)
print("Doubled:", numbers * 2)
print("Squared:", numbers ** 2)
print("Add 10 to each:", numbers + 10)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("a + b:", a + b)
print("a * b:", a * b)


# ===== 5. USEFUL FUNCTIONS =====
print("\n" + "=" * 40)
print("PART 5: USEFUL FUNCTIONS")
print("=" * 40)

data = np.array([4, 8, 15, 16, 23, 42])
print("Data:", data)
print("Sum:", np.sum(data))
print("Mean (average):", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Standard Deviation:", np.std(data))

flat = np.arange(1, 7)
print("\nFlat array:", flat)
reshaped = flat.reshape(2, 3)
print("Reshaped to 2x3:\n", reshaped)