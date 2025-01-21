class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        '''
        [0, 0]
        [0, 1]
        [1, 0]
        [2, 0]
        [1, 1]
        [0, 2]
        [1, 2]
        [2, 1]
        [2, 2]

        direction = upwards or downwards
        we're decrementing r and incrementing c when going upwards
        we're incrementing r and decrementing c when going downwards
        '''

        ROW, COL = len(mat), len(mat[0])
        r,c = 0,0
        res = []
        direction = "upwards"

        while len(res) < ROW * COL:
            res.append(mat[r][c])
            if direction == "upwards":
                if c == COL - 1:
                    direction = "downwards"
                    r += 1
                elif r == 0:
                    direction = "downwards"
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == ROW - 1:
                    c += 1
                    direction = "upwards"
                elif c == 0:
                    r += 1
                    direction = "upwards"
                else:
                    r += 1
                    c -= 1
        return res

