class Solution:
    def isPalindrome(self, text: str):
        text = text.lower()

        if text == text[::-1]:
            print(f'"{text}" is a Palindrome.')
        else:
            print(f'"{text}" is Not a Palindrome.')