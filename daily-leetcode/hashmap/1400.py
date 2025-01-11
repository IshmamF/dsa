from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        elif len(s) == k:
            return True
        count = Counter(s)
        odd = 0
        for val in count.values():
            if val % 2 == 1:
                odd += 1
        if odd > k:
            return False
        else:
            return True
