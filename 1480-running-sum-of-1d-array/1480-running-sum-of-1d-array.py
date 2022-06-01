class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        b = [] 
        b.append(nums[0])
        for i in range(1, len(nums)) :
            b.append(nums[i] + b[i-1])
            
        return b
            
            

            