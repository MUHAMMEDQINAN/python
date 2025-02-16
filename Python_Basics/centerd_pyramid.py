# problem: print a centerd pyramid with the given number of rows

# ✅ Method 1: Using a simple for loop
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# ✅ Method 2: Using a list comprehension
[print(" " * (n - i) + "*" * (2 * i - 1)) for i in range(1, n + 1)]
