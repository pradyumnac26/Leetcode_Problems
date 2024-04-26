class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for i in range(n - 2, -1, -1):
            next_row = grid[i + 1]  
            min1, min2 = sorted(next_row)[:2]
            for j in range(n):
                grid[i][j] += min2 if grid[i + 1][j] == min1 else min1
        return min(grid[0])
        