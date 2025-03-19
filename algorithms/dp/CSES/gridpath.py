from typing import List
grid = [['•', '•', '•', '•'],
        ['•', '*', '•', '•'],
        ['•', '•', '•', '*'],
        ['*', '•', '•', '•']]

def gridPath(n: int, grid: List[List[str]]) -> int:
    dp = {}
    
    def findPaths(x: int = 0, y: int = 0) -> int:
        if (x, y) in dp:
            return dp[(x,y)]
        if x == n - 1 and y == n - 1:
            return 1
        if x >= n or y >= n or grid[x][y] == '*':
            return 0
            
        count = 0
        count += findPaths(x + 1, y)
        count += findPaths(x, y + 1)
        
        dp[(x,y)] = count
        return count 
    return findPaths()
print(gridPath(4, grid))