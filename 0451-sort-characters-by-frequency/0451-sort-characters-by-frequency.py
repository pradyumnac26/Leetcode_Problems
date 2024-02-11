class Solution:
    def frequencySort(self, s: str) -> str:
        x = Counter(s).most_common()
        z = ""
        for c,f in x :
            z = z + c*f
        return z
       
        