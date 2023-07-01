class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        v=['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in v:
                l.append(i)
        ss=""
        for j in s:
            if j in v:
                ss+=l[-1]
                l.pop(-1)
            else:
                ss+=j
        return ss