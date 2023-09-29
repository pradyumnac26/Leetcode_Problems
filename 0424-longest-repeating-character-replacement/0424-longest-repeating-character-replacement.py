class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r-l+1) - max(count.values()) <= k:
                res = max(res, r-l+1)
            else :
                count[s[l]] = count[s[l]] -1
                l = l+1
        return res
            
            
            