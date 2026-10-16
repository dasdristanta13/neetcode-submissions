class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = {}
        for n in nums:
            if n in has:
                return True
            has[n] = 1
        return False