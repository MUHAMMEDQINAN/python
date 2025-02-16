# Problem: Take an integer input and check if it's a palindrome.

# ✅ Method 1: Using string comparison
num = input("Enter a number: ")
print("Palindrome" if num == num[::-1] else "Not a palindrome")

# ✅ Method 2: Using a while loop
num = int(input("Enter a number: "))
orig, rev = num, 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Palindrome" if orig == rev else "Not a palindrome")
