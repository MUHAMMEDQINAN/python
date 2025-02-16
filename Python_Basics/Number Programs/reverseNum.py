# Problem: Take an integer input and print its reverse.

# ✅ Method 1: Using string slicing
num = input("Enter a number: ")
print("Reversed number:", num[::-1])

# ✅ Method 2: Using while loop
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)

# ✅ Method 3: Using recursion
def reverse_number(n, rev=0):
    return rev if n == 0 else reverse_number(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))
