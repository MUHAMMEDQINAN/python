
n = int(input("Enter the number of rows: "))

# horizontal line with stars
print("*" * n)

print("\n\n")

# vertical line with stars
for i in range(n):
    print("*")

print("\n\n")

# horizontal line with stars
for i in range(n):
    print("*", end=" ")

print("\n\n")

# square with stars
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print("\n\n")

# right triangle with stars
for i in range(n):
    for  j in range(i+1):
        print("*", end=" ")
    print()

print("\n\n")

# inverted right triangle with stars
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

print("\n\n")

# left triangle with stars

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

print("\n\n")

# inverted left triangle with stars
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")  # Printing spaces
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("\n\n")

# pyramid with stars
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print("\n\n")

# inverted pyramid with stars
for i in range(n):
    for j in range(i):
        print(" ",end = " ")
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()

print("\n\n")

# diamond with stars
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(n-i-2):
        print("*",end=" ")
    print()

