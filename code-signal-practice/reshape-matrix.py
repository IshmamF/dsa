class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        '''

        '''
        ROW, COL = len(mat), len(mat[0])
        if r * c != ROW * COL:
            return mat
        res = []
        colVals = []
        
        for i in range(ROW):
            for j in range(COL):
                val = mat[i][j]
                colVals.append(val)
                if len(colVals) == c:
                    res.append(colVals.copy())
                    colVals = []
        return res