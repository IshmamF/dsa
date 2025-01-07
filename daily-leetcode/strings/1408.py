class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []

        for i in range(len(words)):
            word = words[i]
            leftSide = ' '.join(words[:i])
            print(leftSide)
            rightSide = ' '.join(words[i+1:]) if i != len(words) - 1 else []
            print(rightSide)
            if word in leftSide or word in rightSide:
                ans.append(word)

        return ans
            