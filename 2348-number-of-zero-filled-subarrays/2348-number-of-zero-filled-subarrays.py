class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count,res = 0,0 
        for i in range(len(nums)):
            if nums[i] == 0 :
                count +=1 
            else :
                count = 0
            res = res + count
        return res
        