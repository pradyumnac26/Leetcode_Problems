class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [] 
        for i in range(len(intervals)) :
            start = intervals[i][0]
            end = intervals[i][1]
            if ans and end <= ans[-1][-1]:
                continue 
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= end : 
                    end = max(end, intervals[j][1])
                else :
                    break 
            ans.append([start, end])
        return ans
                    
                
                
        
        
        