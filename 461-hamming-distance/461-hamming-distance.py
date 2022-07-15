class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        z = bin(z)
        return z.count('1')
     
        

            
        