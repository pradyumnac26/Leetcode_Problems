class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxnum = max(nums)
        count = 0
        long = 1
        for i in range(len(nums)): 
            if nums[i] == maxnum:
                count = count + 1
                long = max(count, long)
            else : 
                count = 0
            
        return long
                
            
                
            
        