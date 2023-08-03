class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}   
        for word in strs:
            sort_word="".join(sorted(word))
            if sort_word not in d:
                d[sort_word]=[word]
            else:
                d[sort_word].append(word)
        result=[]
        for i in d.values():
            result.append(i)
        return result
        
        