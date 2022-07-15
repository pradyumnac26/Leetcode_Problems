class Solution:
    def countBits(self, n: int) -> List[int]:
        b =[] 
        for i in range(n+1):
            x = bin(i)[2:].count('1')
            b.append(x)
        return b
            
            
        
        