class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        '''
        [[1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]]
        '''
        heap = []
        R,C = len(heightMap), len(heightMap[0])
        for r in range(R):
            for c in range(C):
                if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        res = 0
        maxHi = -1
        directions = [[1,0], [-1, 0], [0, 1], [0,-1]]

        while heap:
            h, r, c = heapq.heappop(heap)
            maxHi = max(maxHi, h)
            res += maxHi - h

            for x,y in directions:
                new_r = r + x
                new_c = c + y

                if new_r not in range(R) or new_c not in range(C) \
                or heightMap[new_r][new_c] == -1:
                    continue

                heapq.heappush(heap, (heightMap[new_r][new_c], new_r, new_c))
                heightMap[new_r][new_c] = -1

        return res