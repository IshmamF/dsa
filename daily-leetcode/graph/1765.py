from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        ROW, COL = len(isWater), len(isWater[0])
        directions = [[0, 1], [1,0], [-1,0], [0,-1]]
        ans = [[-1] * COL for _ in range(ROW)]

        for i in range(ROW):
            for j in range(COL):
                if isWater[i][j] == 1:
                    isWater[i][j] = -1
                    q.append((i,j))
                    ans[i][j] = 0

        while q:
            r, c = q.popleft()
            val = ans[r][c]
            
            for dx, dy in directions:
                new_r, new_c = r + dx, c + dy   
                
                if new_r not in range(ROW) \
                or new_c not in range(COL) \
                or isWater[new_r][new_c] == -1:
                    continue

                ans[new_r][new_c] = val + 1
                isWater[new_r][new_c] = -1
                q.append((new_r, new_c))
        return ans
