class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        l = [] 
        for i in nums1 : 
            if i in nums2 :
                l.append(i)
        return l
    
    #nums1.intersection(nums2)
        