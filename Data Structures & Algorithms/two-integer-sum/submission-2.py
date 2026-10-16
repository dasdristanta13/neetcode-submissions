class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            find = target - num
            for j in range(i+1,len(nums)):
                if nums[j] == find:
                    return [i,j]
            