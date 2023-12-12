class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        return max(c, key=c.get)
            
        
        
        