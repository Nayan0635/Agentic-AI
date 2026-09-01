# num = int(input("Enter a number: "))

# if num == 0 or num == 1:
#     print(f"{num} is neither prime nor composite.")
#     exit(0)    
    
# is_prime = True

# # for i in range(2, int(num**0.5) + 1):
# from math import sqrt

# for i in range (2, int(sqrt(num)), 1):
#     if num % i == 0:
#         is_prime = False
#         break
#     print("{i} ")
    
# if is_prime:
#     print(f"{num} is a prime number.") 
# else:
#     print(f"{num} is not a prime number.")


def isPrime(n:int) -> bool: 
    if n == 0 or n == 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True