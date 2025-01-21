class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        [0,0]
        [1,1]
        [2,2]

        [0,1]
        [1,2]
        [2,3]

        [0,2]
        [1,3]

        [1,0]
        [2,1]
        '''
        ROW, COL = len(matrix), len(matrix[0])

        r = 0

        while r < ROW:
            
            for c in range(COL):
                temp_row = r
                val = matrix[temp_row][c]
                temp_c = c
                while temp_row < ROW and temp_c < COL:
                    if matrix[temp_row][temp_c] != val:
                        return False
                    temp_row += 1
                    temp_c += 1
            r += 1
        return True

