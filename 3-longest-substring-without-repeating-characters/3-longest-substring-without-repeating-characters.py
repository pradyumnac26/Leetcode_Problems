class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ start=0
        longest = 0
        dick = {}
        for i in range(len(s)) :
            if s[i] in dick and start <= dick[s[i]]:
                start = dick[s[i]] + 1
            else :
                longest = max(longest,i - start + 1)
            dick[s[i]] = i 
        return longest """
                
                
        maxLen = 0    
        i= 0 
        hmap = defaultdict(int)
        
        for j in range(len(s)) : 
            hmap[s[j]] += 1
            while hmap[s[j]] > 1 :
                hmap[s[i]] -=1 
                i = i +1
            curLen = j -i +1 
            maxLen = max(maxLen,curLen)
            
        return maxLen