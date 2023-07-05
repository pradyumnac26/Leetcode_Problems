class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currsum = 0
        for i in nums :
            if currsum < 0:
                currsum = 0 
            currsum += i
            maxSub = max(maxSub,currsum)
        return maxSub
        
        