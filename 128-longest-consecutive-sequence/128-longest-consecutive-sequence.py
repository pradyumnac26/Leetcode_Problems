class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 1
        long = 1 
        if len(nums) == 0 :
            return 0
        for i in range(1, len(nums) ) :
            if nums[i] != nums[i-1] :
                
                if nums[i] - nums[i-1] ==1 :
                    cnt+=1
                else :
                    long = max(long , cnt)
                    cnt = 1 
        return max(long,cnt)
            
            
        