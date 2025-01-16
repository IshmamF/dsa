from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        '''
        i = 0, count = 0
        [2] & [3] -> 0
        {2: 1, 3: 1}
        i = 1, count = 1
        [2, 3] & [3, 1] -> 1
        {2: 1, 3: 2, 1: 1}
        
        i = 2, count = 3
        [2, 3, 1] & [3, 1, 2] -> 3
        {2: 2, 3: 2, 1: 2}

        A = [1,3,2,4], B = [3,1,2,4]
        i = 0
        visit = (1, 3) -> count = 0

        i = 1
        3 is in visit -> count = 1
        1 is in visit -> count = 2

        i = 2
        A[i] == B[i] -> count = 3

        i = 3
        A[i] == B[i] -> count = 4
        '''
        visit = set()
        res = [0] * len(A)
        count = 0
        for i, (a, b) in enumerate(zip(A, B)):
            if a == b:
                count += 1
            else:
                if a in visit:
                    count += 1
                if b in visit:
                    count += 1
            visit.add(a)
            visit.add(b)
            res[i] = count
        return res
                