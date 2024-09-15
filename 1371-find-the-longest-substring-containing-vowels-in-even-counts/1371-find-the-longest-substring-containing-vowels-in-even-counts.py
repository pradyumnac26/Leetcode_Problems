class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        x = "aeiou"
        mask = 0
        res = 0
        mask_to_idx = {0:-1}
        for i,c in enumerate(s): 
            if c in x: 
                mask = mask ^ (1 + ord(c) - ord('a'))
            if mask in mask_to_idx : 
                length = i - (mask_to_idx[mask])
                res = max(length, res)
            else : 
                mask_to_idx[mask] = i
        return res
        