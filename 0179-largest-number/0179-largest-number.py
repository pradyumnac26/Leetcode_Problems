class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        b = [] 
        for i in nums: 
            b.append(str(i))
        
        b.sort(key = lambda a : a*10, reverse = True)
        print(b)
        
        if b[0] == "0" : 
            return "0"
        
        return "".join(b)
            
        
        
        