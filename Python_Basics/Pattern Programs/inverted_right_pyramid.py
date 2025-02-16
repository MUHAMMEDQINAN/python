# Problem: Print an inverted right-angled triangle with '*'.

n = int(input("Enter the number of rows: "))

# ✅ Method 1: Using a simple loop
for i in range(n, 0, -1):
    print("*" * i)

# ✅ Method 2: Using nested loops
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()