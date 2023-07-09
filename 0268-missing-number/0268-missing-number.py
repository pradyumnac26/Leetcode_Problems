class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         for i in range(len(nums)+1) :
#             if i not in nums :
#                 return i
        res = 0 
        d1 = sum(nums)
        n = len(nums)
        d2 = n*(n+1)//2
        return d2-d1