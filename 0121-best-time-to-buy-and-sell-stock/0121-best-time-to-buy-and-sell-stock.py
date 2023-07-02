class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxp = 0 
        while r < len(prices) :
            if (prices[l] < prices[r]) :
                profit = prices[r] - prices[l]
                maxp = max(profit,maxp)
            else : 
                l = r 
            r = r+1
        return maxp