class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0 
        second = 1
        third = 1
        if n == 0 :
            return first
        if n ==  1 or n == 2 :
            return second
        ans = 0
        for i in range(3, n+1):
            ans = first + second + third
            first,second,third = second, third,ans
            
  
        return ans
            
        
        
             
        