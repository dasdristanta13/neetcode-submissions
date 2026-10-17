class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalnum()])
        space = len(s)
        if space == 0:
            return True
        for i in range(space//2):
            if s[i] != s[space-i-1]:
                return False
        return True