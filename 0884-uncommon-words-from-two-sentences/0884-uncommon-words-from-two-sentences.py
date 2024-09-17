class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        c = Counter(s1.split() + s2.split())
        print(c)
        b = [] 
        for i in c.items(): 
            if i[1] == 1:
                b.append(i[0])
        return b
                
        
        