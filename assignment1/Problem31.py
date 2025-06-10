#GCD of two numbers using loop.
def gcd(a, b):
    # Make sure both numbers are positive
    a, b = abs(a), abs(b)

    # Find the smaller of the two numbers
    min_num = min(a, b)

    # Loop from min_num down to 1
    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

#Example Usage
print(gcd(48, 18))  # Output: 6
