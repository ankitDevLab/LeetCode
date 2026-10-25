class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res=nums[0]
        curr = nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i],curr+nums[i])
            res = max(curr,res)
        return res






