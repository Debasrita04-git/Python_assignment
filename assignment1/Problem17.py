#Print ASCII values of characters in a string.
# Get input from the user
text = input("Enter a string: ")

# Print ASCII value for each character
for char in text:
    print(f"ASCII value of '{char}' is {ord(char)}")
