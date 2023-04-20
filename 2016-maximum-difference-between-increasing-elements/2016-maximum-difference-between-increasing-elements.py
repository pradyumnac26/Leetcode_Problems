class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = nums[0]
        maxi = -1
        for i in range(1, len(nums)) :
            if (nums[i] - mini > maxi) :
                maxi = nums[i] - mini
                
            if nums[i] < mini :
                mini = nums[i]
        if maxi > 0 :
            return maxi
        else : 
            return -1
        