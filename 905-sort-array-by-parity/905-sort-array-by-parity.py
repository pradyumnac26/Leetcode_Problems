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
    