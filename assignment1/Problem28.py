#Sum of even numbers in a list.
def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Example usage
my_list = [1, 2, 3, 4, 5, 6]
print(f"Sum of even numbers: {sum_of_even_numbers(my_list)}")
