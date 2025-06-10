#Count frequency of digits in a number.
def count_digit_frequency(number):
    freq = {}
    for digit in str(abs(number)):  # Convert to string and handle negative numbers
        if digit.isdigit():  # Ensure only digits are counted
            freq[digit] = freq.get(digit, 0) + 1
    return freq

#Example Usage
result = count_digit_frequency(112358112)
print(result)
