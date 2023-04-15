class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1] : 
            return True
        else : 
            return False

        #        if x < 0:
         #   return False
        #       rev = 0
        #       orig = x
        #       while x != 0:
            #   rev = rev * 10 + x % 10
            #       x //= 10
        #       return rev == orig