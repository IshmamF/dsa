n = int(input())
grid = []

for _ in range(n):
    row = input()
    grid.append(list(row))

MOD = 10**9 + 7

def gridPath(n, grid):
    dp = {}
    
    def findPaths(x: int = 0, y: int = 0) -> int:
        if (x, y) in dp:
            return dp[(x,y)]
        if x == n - 1 and y == n - 1 and grid[x][y] != '*':
            return 1
        if x >= n or y >= n or grid[x][y] == '*':
            return 0
            
        count = (findPaths(x + 1, y) + findPaths(x, y + 1)) % MOD
        
        dp[(x,y)] = count
        return count 
    return findPaths()

print(gridPath(n, grid))