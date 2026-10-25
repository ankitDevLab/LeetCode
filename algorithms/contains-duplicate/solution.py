class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        mink=prices[0]
        maxk=prices[0]
        for i in prices:
            if i < mink:
                mink=i
                maxk=i
            if i > maxk:
                maxk=i
            if maxk - mink > profit:
                profit = maxk - mink
        return profit