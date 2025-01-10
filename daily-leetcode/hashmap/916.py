from collections import Counter
from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2 = set(words2) # Remove duplicates 
        allLetters = {}
        '''
        We want to preprocess words2 and total all the necessary letters into one dictionary so we
        can just reference that for every word in words1. Also going through the allLetters map is
        O(1) because most amount of letters we can have is 26. We take the max of the count of any
        letter we see again since if a word has the highest instance of a given a letter, any
        instance less than that would also be valid.
        '''
        for word in words2: 
            count = Counter(word)
            for key,val in count.items():
                if key not in allLetters:
                    allLetters[key] = val
                else:
                    allLetters[key] = max(allLetters[key], val)

        res = []
        for word in words1:
            count = Counter(word)
            addWord = True
            for key,val in allLetters.items():
                if key not in count or val > count[key]:
                    addWord = False
                    break
            if addWord:
                res.append(word)

        
        return res