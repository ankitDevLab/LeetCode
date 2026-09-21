class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict={}
        for i in range(len(nums)):
            need=target-nums[i]
            if mydict.get(need) != None:
                return (i,mydict.get(need))
            else:
                mydict[nums[i]]=i
        return []
        
        