class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0 :
            return 0
        n=bin(n)[2:]
        if n.count('1')==1:
            return 1 
        else :
            return 0

        