#Count uppercase and lowercase letters in a string
def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

#Example Usage
upper, lower = count_upper_lower("Hello World!")
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
