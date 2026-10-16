class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i,num in enumerate(nums):
            if (target - num) in target_dict:return [target_dict[target-num],i]
            target_dict[num] = i
            