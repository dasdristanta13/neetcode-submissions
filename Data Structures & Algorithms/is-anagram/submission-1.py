class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        Count = {}
        for i in range(len(s)):
            Count[s[i]] = 1 + Count.get(s[i],0)
            Count[t[i]] = Count.get(t[i],0) - 1
        return not any(Count.values())