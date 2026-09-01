def isPalindrome(n:int) -> bool:
    temp = n
    reverse = 0
    
    while temp > 0:
        digits = temp % 10
        reverse = reverse * 10 + digits
        temp = temp // 10
        
    return n == reverse