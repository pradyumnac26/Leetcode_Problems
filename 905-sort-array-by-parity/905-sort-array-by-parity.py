class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        b = []
        q = []
        for i in nums :
            if i%2  == 0 :
                b.append(i)
            else :
                q.append(i)

        return b+q
    
    # A.sort(key = lambda x : x%2) as even number remainder will be 0 and for odd it is 1 , so sort it .