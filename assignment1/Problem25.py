#Reverse a number using loop.
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

# Example usage
number = 12345
print(f"Reversed number: {reverse_number(number)}")
