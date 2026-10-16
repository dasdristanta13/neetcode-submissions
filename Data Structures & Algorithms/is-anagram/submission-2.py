class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if len(s)==0:
            return True
        seen = {}
        for s_char in s:
            seen[s_char] = seen.get(s_char,0)+1
        for t_char in t:
            seen[t_char] = seen.get(t_char,0)-1
        if all([val == 0 for val in seen.values()]):
            return True
        return False