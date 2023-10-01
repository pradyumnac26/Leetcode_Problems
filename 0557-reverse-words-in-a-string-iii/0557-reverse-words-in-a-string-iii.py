class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        b = []
        for i in words :
            b.append(i[::-1])
        return ' '.join(b)
        
            
            
        