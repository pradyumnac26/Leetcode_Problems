class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        while(l<=r) :
            mid = (l+r)//2
            if nums[mid] == target :
                return mid
            
            #if the mid is in the left sorted portion then 
            if nums[l] <= nums[mid] :
                if target < nums[l] or target > nums[mid] :
                    l = mid+1
                else : 
                    r = mid-1
            #right sorted portion
            else :
                if target < nums[mid] or target > nums[r] :
                    r = mid-1 
                else :
                    l = mid+1
        return -1