class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        b = [] 
        d = len(matrix[0])
        for i in range(d):
            x = []
            for j in range(len(matrix)):
                
                x.append(matrix[j][i])
            b.append(x)
        return b
                

        