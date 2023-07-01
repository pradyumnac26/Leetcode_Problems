class Solution:
    def reverseWords(self, s: str) -> str:
        v = s.split(' ')
        print(v)
        q = []
        v.reverse()
        for i in range(len(v)) : 
            if v[i] != "" :
                q.append(v[i])
        return ' '.join(q)
        