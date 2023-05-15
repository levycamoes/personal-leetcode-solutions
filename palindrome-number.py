class Solution:
    def isPalindrome(self, x: int) -> bool: 
        for i in str(x).split():
            if i == i[::-1]:
                return True
            else:
                return False
