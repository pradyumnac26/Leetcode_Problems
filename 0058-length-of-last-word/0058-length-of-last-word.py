class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = []
        s = s.split(' ')
        print(s)
        for i in s : 
            if i != '' :
                b.append(i)
        return len(b[-1])
                
        