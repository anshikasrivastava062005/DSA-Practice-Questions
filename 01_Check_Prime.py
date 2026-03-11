'''
Check if a Number is Prime:
Problem: Write a function to check if a given number is prime.
Input: Number: 29
Output: True
Explanation: 29 is a prime number
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
num = 29
print(is_prime(num))