class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0]*len(nums)
        i = len(nums) - 1 
        prev_max = 0 
        
        for n in reversed(nums) : 
            max_right[i] = max(prev_max, n )
            prev_max = max_right[i]
            i= i-1
        
        l=0
        res = 0 
        for r in range(len(nums)) : 
            while nums[l] > max_right[r] : 
                l = l+1
            
            res = max(res,r-l )
        return res
            
        
                
        