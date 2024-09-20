class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        n = len(s)
        P, MOD, POW = 31, 10**9 + 7, 1
        h1 = h2 = max_pan_pref_len = 0
        for i in range(n):
            char_int = ord(s[i]) - ord("a") + 1
            h1 = (h1 * P + char_int) % MOD
            h2 = (char_int * POW + h2) % MOD
            if h1 == h2: max_pan_pref_len = i + 1
            POW = POW * P % MOD

        return s[max_pan_pref_len:][::-1] + s   
        