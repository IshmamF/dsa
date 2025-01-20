from typing import List
'''
Intuition: We premake the matrix, and then using the code/intuition from spiral matrix 1
we set current (row, column) to num.   
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        L, R = 0, len(matrix[0])
        T, B = 0, len(matrix)

        num = 1
        while L < R and T < B:
            for i in range(L, R):
                matrix[T][i] = num
                num += 1
            T+=1

            for j in range(T, B):
                matrix[j][R-1] = num
                num += 1
            R-=1

            if L >= R or T >= B:
                break
            
            for k in range(R-1, L-1, -1):
                matrix[B-1][k] = num
                num += 1
            B-=1

            for l in range(B-1, T-1, -1):
                matrix[l][L] = num
                num += 1
            L+=1
        return matrix