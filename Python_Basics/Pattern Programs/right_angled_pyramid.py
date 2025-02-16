# Problem: Print a right-angled triangle with '*' of height 'n'.

n = int(input("Enter the number of rows: "))

# ✅ Method 1: Using a simple for loop
for i in range(1, n + 1):
    print("*" * i)

# ✅ Method 2: Using nested loops
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# ✅ Method 3: Using a list comprehension
[print("*" * i) for i in range(1, n + 1)]
