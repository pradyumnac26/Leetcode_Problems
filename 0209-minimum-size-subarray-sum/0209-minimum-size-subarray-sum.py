class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        total = 0 
        res = float('inf')
        for r in range(len(nums)) : 
            total = total + nums[r] 
            while total >= target :
                res = min(res, r-l+1)
                total = total - nums[l]
                l = l + 1 
        return 0 if res == float('inf') else res 
                
            
            
        