from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        '''
        aaa -> a
        aaaa -> aa 
        aaaaa -> a
        '''
        count = Counter(s)
        for char, freq in count.items():
            count[char] = 1 if freq % 2 == 1 else 2
        return sum(count.values())
        
