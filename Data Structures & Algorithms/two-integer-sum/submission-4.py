class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i,num in enumerate(nums):
        #     find = target - num
        #     for j in range(i+1,len(nums)):
        #         if nums[j] == find:
        #             return [i,j]
        target_dict = {}
        for i,num in enumerate(nums):
            if (target - num) in target_dict:
                return [target_dict[target-num],i]
            target_dict[num] = i
            