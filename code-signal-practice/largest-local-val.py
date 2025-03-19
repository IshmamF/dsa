class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        ROW, COL = len(grid), len(grid[0])
        output = [[0] * (COL - 2) for _ in range(ROW - 2)]

        for r in range(1, ROW - 1):

            for c in range(1, COL - 1):

                top = grid[r-1][c]
                topLeft = grid[r-1][c-1]
                topRight = grid[r-1][c+1]
                topMax = max(top, topLeft, topRight)

                bottom = grid[r+1][c]
                bottomLeft = grid[r+1][c-1]
                bottomRight = grid[r+1][c+1]
                current = grid[r][c]
                bottomMax = max(bottom, bottomLeft, bottomRight,current)

                left = grid[r][c-1]
                right = grid[r][c+1]
                output[r-1][c-1] = max(left,right,topMax,bottomMax)
        return output
                
