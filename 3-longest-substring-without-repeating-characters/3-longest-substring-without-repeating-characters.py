class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        longest = 0
        dick = {}
        for i in range(len(s)) :
            if s[i] in dick and start <= dick[s[i]]:
                start = dick[s[i]] + 1
            else :
                longest = max(longest,i - start + 1)
            dick[s[i]] = i 
        return longest
                
                
                                        
        