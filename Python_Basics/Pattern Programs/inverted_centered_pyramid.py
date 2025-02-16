# Problem: Print an inverted full pyramid.

n = int(input("Enter the number of rows: "))

# ✅ Method 1: Using a for loop
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# ✅ Method 2: Using a list comprehension
[print(" " * (n - i) + "*" * (2 * i - 1)) for i in range(n, 0, -1)]

# ✅ Method 3: Using nested loops
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()