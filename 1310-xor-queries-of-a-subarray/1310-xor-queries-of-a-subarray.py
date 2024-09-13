class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        b = [] 
        prefix_xor = [0]*(len(arr) + 1)
        for i in range(len(arr)): 
            prefix_xor[i+1] = prefix_xor[i] ^ arr[i]
            
        for x,y in queries : 
            b.append(prefix_xor[y+1] ^ prefix_xor[x])
        return b
            
            
            
            
                
    
