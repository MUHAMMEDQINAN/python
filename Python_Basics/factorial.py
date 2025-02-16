# Problem: Take a number and compute its factorial.

# ✅ Method 1: Using a for loop
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

# ✅ Method 2: Using recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

# ✅ Method 3: Using math library
import math
num = int(input("Enter a number: "))
print("Factorial:", math.factorial(num))
