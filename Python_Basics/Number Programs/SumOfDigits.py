# Problem: Take an integer input and find the sum of its digits.

# ✅ Method 1: Using a while loop
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10  # Extract last digit and add to sum
    num //= 10  # Remove last digit
print("Sum of digits:", sum_digits)

# ✅ Method 2: Using recursion
def sum_of_digits(n):
    return n if n < 10 else (n % 10) + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))

# ✅ Method 3: Using list comprehension and sum() function
num = input("Enter a number: ")
sum_digits = sum(int(digit) for digit in num)
print("Sum of digits:", sum_digits)
