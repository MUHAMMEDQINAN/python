# Problem: Take three numbers as input and print the largest one.

# ✅ Method 1: Using max() function
a, b, c = map(int, input("Enter three numbers: ").split())
print("Largest number:", max(a, b, c))


# ✅ Method 2: Using if-elif-else
a, b, c = map(int, input("Enter three numbers: ").split())
if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


# ✅ Method 3: Using list and sort()
numbers = list(map(int, input("Enter three numbers: ").split()))
numbers.sort()
print("Largest number:", numbers[-1])
