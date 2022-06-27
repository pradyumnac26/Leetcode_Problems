class Solution:
    def minPartitions(self, n: str) -> int:
        b = []
        for i in n :
            b.append(int(i))
        return max(b)
        
        
            
        #max(n)