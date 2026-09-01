class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing={}
        num="x"
        for i in nums:
            missing[i]=1
        for i in range(len(nums)+1):
            if i not in missing:
                num=i
                break
        return num