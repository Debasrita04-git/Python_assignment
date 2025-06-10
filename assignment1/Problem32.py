#Check if a number is a palindrome.
def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

#Example Usage
print(is_palindrome(121))   # True
print(is_palindrome(123))   # False
print(is_palindrome(1221))  # True
 