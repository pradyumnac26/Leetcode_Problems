class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        min_element = prices[0]
      
        for i in range( 1, len(prices) ):
            if (prices[i] - min_element > max_diff):
                max_diff = prices[i] - min_element
      
            if (prices[i] < min_element):
                min_element = prices[i]
        return max_diff
        