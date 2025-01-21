class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Neetcode soluiton intuition:
        we're moving 
        storing top left value 
        bottom left to top left
        bottom right to bottom left
        top right to bottom right
        then placing stored value at top right

        while loop iteration is about the outer box of the matrix
        i in for loop represents current part of the outer box we're moving
        """
        L, R = 0, len(matrix) - 1
        T, B = 0, len(matrix[0]) - 1

        while L < R and T < B:
            for i in range(R-L):

                topleft = matrix[T][L + i]

                matrix[T][L + i] = matrix[B - i][L]

                matrix[B - i][L] = matrix[B][R - i]

                matrix[B][R - i] = matrix[T+i][R]

                matrix[T+i][R] = topleft

            L += 1
            R -= 1
            T += 1
            B -= 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        '''
        Intuition: Transposing and then doing a horizontal reflection
        achieves the rotation. 
        '''
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            for j in range(n // 2):
                # n-j-1 is similar to two pointer problems to go in reverse 
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
