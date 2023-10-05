class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0 
        x = Counter(nums)
        for ind,val in x.items():
            res =  res + (val*(val-1))//2
        return res
            
        