#Swap two numbers using a temporary variable.
# Input two numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Swap using a temporary variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
