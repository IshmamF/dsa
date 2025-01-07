# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-01-04

def countPalindromicSubsequence(s: str) -> int:
    """
    [[], [b], [b, c], [b, b, c], [b, b, c, b], [b, b, c, b, a], [b, b, c, b, a, b]]
    """

    leftSide = set()
    rightSide = [None] * len(s)
    curr = set()
    for r in range(len(s)-1, -1, -1):
        char = s[r]
        rightSide[r] = curr.copy()
        curr.add(char)
    leftSide.add(s[0])
    hashSet = set()
    for i in range(1, len(s)-1):
        rightChars = rightSide[i]

        for c in leftSide:
            if c in rightChars:
                currentPalindrome = c + s[i] + c
                hashSet.add(currentPalindrome)
        leftSide.add(s[i])
    return len(hashSet)