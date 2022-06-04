class Solution:
    def reverse(self, x: int) -> int:
 
        rev = int(str(abs(x))[::-1])
        

        if x < 0 and (rev.bit_length() < 32) :
            return -rev 
        elif x>0 and rev.bit_length() < 32 :
            return rev
        else :
            
            return 0
        

        
