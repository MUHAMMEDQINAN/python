# Problem: Take an integer input and count how many digits it has.

# ✅ Method 1: Using len() function
num = input("Enter a number: ")
print("Number of digits:", len(num))

# ✅ Method 2: Using while loop
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)
