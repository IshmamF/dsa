# Problem Link: https://leetcode.com/problems/count-vowel-strings-in-ranges/description/?envType=daily-question&envId=2025-01-02

def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    vowels = ['a', 'o', 'i', 'u', 'e']
    translateToNums = []

    for word in words:
        if word[0] in vowels and word[-1] in vowels:
            translateToNums.append(1)
        else:
            translateToNums.append(0)

    prefixSumList = []
    tempSum = 0
    for n in translateToNums:
        tempSum += n
        prefixSumList.append(tempSum)
    
    def findPrefixSum(L, R):
        right = prefixSumList[R]
        left = prefixSumList[L-1] if L > 0 else 0
        return right - left
        
    result = []
    for query in queries:
        value = findPrefixSum(query[0], query[1])
        result.append(value)
    return result