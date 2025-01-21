from collections import deque, defaultdict
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque() 
        q.append((0,0))
        dists = defaultdict(lambda:inf)
        dists[(0,0)] = 0

        directions = [[1,0,1], [3,1,0], [2,0,-1], [4,-1,0] ]

        while q:
            x,y = q.popleft()

            if x == R-1 and y == C-1:
                return dists[x,y]

            for d, dirX, dirY in directions:
                new_x = x + dirX
                new_y = y + dirY
                if new_x not in range(R) or new_y not in range(C):
                    continue

                add_cost = 0
                if d != grid[x][y]:
                    add_cost = 1

                if dists[new_x,new_y] > add_cost + dists[x,y]:
                    dists[new_x,new_y] = add_cost + dists[x,y]

                    if add_cost:
                        q.append((new_x,new_y))
                    else:
                        q.appendleft((new_x,new_y))

            
