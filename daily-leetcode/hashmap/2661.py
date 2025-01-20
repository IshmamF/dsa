from collections import defaultdict
from typing import List
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        '''
        [6,2,3,1,4,5]

        [5,1]
        [2,4]
        [6,3]

        '''
        R, C = len(mat), len(mat[0])
        hashmap = {}
        for i in range(R):
            for j in range(C):
                hashmap[mat[i][j]] = (i, j)
        rowMap, colMap = defaultdict(int), defaultdict(int)
        
        for i, paint in enumerate(arr):
            r, c = hashmap[paint]
            rowMap[r] += 1
            colMap[c] += 1

            if colMap[c] == R or rowMap[r] == C:
                return i

