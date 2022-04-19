class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        resultGrid = grid
        for i in range(k):
            newGrid = [[0]*n for i in range(m)]
            if n != 1:
                for i in range(m):
                    for j in range(n-1):
                        newGrid[i][j+1] = grid[i][j]
                        if j == n-2 and i != m-1:
                            newGrid[i+1][0] = grid[i][n-1]
                newGrid[0][0] = grid[m-1][n-1]
                grid = newGrid
            else:
                for i in range(m-1):
                    newGrid[i+1][0] = grid[i][0]
                newGrid[0][0] = grid[m-1][0]
                grid = newGrid  
        return grid
        