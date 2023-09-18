class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        b = []
        for i in mat:
                b.append(i.count(1))
                
        print(b)
        indices = list(range(len(b)))
        indices.sort(key = lambda i : b[i])
        print(indices)
        return indices[:k]
        
        
        
        
        
                
    