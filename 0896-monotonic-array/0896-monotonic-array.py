class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        
        inc = True
        des = True
        
        for i in range(len(nums)-1):
            
            if(nums[i] > nums[i+1]):
                inc = False
            elif(nums[i] < nums[i+1]):
                des = False
        
        return inc or des
    
            
        
        