#Find the maximum in a list using loop.
def find_max(numbers):
    if not numbers:
        return None  # Handle empty list
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Example usage
my_list = [3, 7, 2, 9, 5]
print(f"Maximum number: {find_max(my_list)}")
