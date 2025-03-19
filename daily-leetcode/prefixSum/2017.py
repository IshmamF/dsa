class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        gridLength = len(grid[0])
        if gridLength == 1:
            return 0
        elif gridLength == 2:
            return min(grid[0][1], grid[1][0])

        curr1 = 0
        curr2 = 0
        for i in range(gridLength):
            curr1 += grid[1][i]
            grid[1][i] = curr1

            j = gridLength - i - 1
            curr2 += grid[0][j]
            grid[0][j] = curr2

        robotMin = float('inf')
        for i in range(gridLength - 1):
            if i == 0:
                robotVal = grid[0][1]
                robotMin = min(robotMin, robotVal)
            else:
                maxVal = max(grid[0][i+1], grid[1][i-1])
                robotMin = min(maxVal, robotMin, grid[1][gridLength-2])
        return robotMin

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        gridLength = len(grid[0])
        if gridLength == 1:
            return 0
        elif gridLength == 2:
            return min(grid[0][1], grid[1][0])

        totalSum = sum(grid[0])
        curr = 0

        robotMin = totalSum
        for i in range(0, gridLength):
            totalSum -= grid[0][i]
            currMax = max(totalSum, curr)
            curr += grid[1][i]
            robotMin = min(robotMin, currMax)

        return robotMin
        