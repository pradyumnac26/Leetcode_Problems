class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        x = set()
        for i in range(len(s) - k +1) :
            x.add(s[i:i+k])
        if len(x) == 2**k :
            return 1 
        else:
            return 0

        