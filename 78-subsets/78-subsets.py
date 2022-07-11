class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        b = [] 
        for i in range(2**n, 2**(n+1)) :
            bitmask = bin(i)[3:]
            q=[]
            for j in range(n) :
                if bitmask[j] == '1' :
                    q.append(nums[j])
            b.append(q)
        return b
                    
                
            
            
        