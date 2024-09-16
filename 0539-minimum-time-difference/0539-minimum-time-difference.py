class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        b = [] 
        for i in timePoints: 
            hours, mins = map(int, i.split(":"))
            minutes = 60*hours + mins
            if minutes == 0:
                minutes = 1440
            b.append(minutes)
            
        b.sort()
            
        z = float('inf')
        for i in range(1, len(b)):
            z = min(z, abs(b[i] - b[i-1]) )
        
        return min(z, 1440 - b[-1] + b[0] )
            
            
        
        
        
            
            
        
        
        
        