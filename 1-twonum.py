class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            tmp_nums = nums[i+1::]
            if target - nums[i] in tmp_nums:
                return i, tmp_nums.index(target - nums[i]) + (len(nums) - len(tmp_nums))