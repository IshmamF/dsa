from collections import Counter
from typing import List
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        '''
        derived : [1, 1, 0] // two 1s, one 0
        original : [0, 1, 0]

        derived : [1, 1] // two 1s, zero 0s
        original : [0, 1]

        derived : [1,0,1,0,1,0] // three 1s, three 0s
        not possible

        derived : [1,1,1,0,0,0] // three 1s, three 0s
        not possible

        derived : [1,0,1,0,1,1] // four 1s, 2 zeros
        original : [0,1,1,0,0,1]
        '''
        count = Counter(derived)
        num1s = 0
        if 1 in count:
            num1s = count.get(1)
        return num1s % 2 == 0 if num1s != 0 else True