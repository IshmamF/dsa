from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        rowCount = [0] * ROW
        colCount = [0] * COL

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1

        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (rowCount[r] > 1 or colCount[c] > 1):
                    res += 1
        return res
