class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        [1, 2, 3]
        [4, 5, 6]

        [1, 4]
        [2, 5]
        [3, 6]
        '''
        
        ROW, COL = len(matrix), len(matrix[0])

        res = []
        for c in range(COL):
            rowVal = []
            for r in range(ROW):
                rowVal.append(matrix[r][c])
            res.append(rowVal)

        return res