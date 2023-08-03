class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        count = 1
        currmax = 1
        for i in range(1,len(nums)) :
            if nums[i] - nums[i-1] == 1 :
                count = count + 1 
            else : 
                count = 1
            if count > currmax : 
                currmax = count 
        return currmax if len(nums) !=0 else 0

