n = int(input("Enter a number: "))

from Palindrome import isPalindrome
from Prime import isPrime

if isPalindrome(n) and isPrime(n):
    print(f"{n} is a PalPrime number.")