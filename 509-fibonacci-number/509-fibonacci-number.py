class Solution:
    def fib(self, n: int) -> int:
        x = 0 
        y = 1
        z= 0 
        if n == 0 :
            return 0
        if n == 1 :
            return 1

        else :
            for i in range(2, n+1) :
                z = x + y
                x = y 
                y = z
            
        return z  
        