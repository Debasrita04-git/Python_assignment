#Find the factorial of a number.
# Factorial using a loop
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
number = 5
print(f"Factorial of {number} is {factorial(number)}")
