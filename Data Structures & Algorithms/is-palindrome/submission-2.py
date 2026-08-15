class Solution:
    def isPalindrome(self, s: str) -> bool:
        res  = ''.join(c.lower()for c in s if c.isalnum())
        ser  = res[::-1]
        if ser==res:
            return True
        else:
            return False
        