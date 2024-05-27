class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix) , len(matrix[0])
        isZeroRow = False

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        isZeroRow = True
                
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                
        
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0
        
        if isZeroRow:
            for col in range(cols):
                matrix[0][col] = 0