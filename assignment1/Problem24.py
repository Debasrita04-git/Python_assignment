#Count vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
text = "Hello, World!"
print(f"Number of vowels: {count_vowels(text)}")
