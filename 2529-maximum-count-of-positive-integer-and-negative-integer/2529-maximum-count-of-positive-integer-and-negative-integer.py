class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cntpos = 0
        cntneg = 0
        for i in nums : 
            if i > 0:
                cntpos+=1
            elif i< 0 :
                cntneg+=1
        return max(cntpos,cntneg)
                
        