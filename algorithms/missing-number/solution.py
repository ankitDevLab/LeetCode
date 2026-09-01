class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        k=k%n
        l1=nums[:n-k]
        l2=nums[n-k:]
        nums[:k]=l2
        nums[k:]=l1

        