from typing import List

'''
Intuition: We have 4 pointers, that pretty much shrinks the matrix. 
We're handling each row/col one at a time.
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        L, R = 0, len(matrix[0])
        T, B = 0, len(matrix)

        while L < R and T < B:
            for i in range(L, R):
                res.append(matrix[T][i])
            T+=1

            for j in range(T, B):
                res.append(matrix[j][R-1])
            R-=1

            if L >= R or T >= B:
                break
            
            for k in range(R-1, L-1, -1):
                res.append(matrix[B-1][k])
            B-=1

            for l in range(B-1, T-1, -1):
                res.append(matrix[l][L])
            L+=1
        return res
    
