class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s= ""
        for i in digits : 
            s = s+ str(i)
        t = int(s)
        t = t + 1
        s = str(t)
        v = [] 
        for i in s : 
            v.append(int(i))
        return v
        