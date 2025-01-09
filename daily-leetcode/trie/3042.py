class TrieNode:
    def __init__(self):
        self.words = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.words:
                curr.words[c] = TrieNode()
            curr = curr.words[c]
    
    def searchWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.words:
                return False
            curr = curr.words[c]
        return True

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        reverseMap = {}
        for word in words:
            reverseMap[word] = word[::-1]
        count = 0

        for i in range(len(words)-1):
            currWord = words[i]
            reversedCurrWord = reverseMap[currWord]

            for word in words[i+1:]:
                prefixTrie = Trie()
                postfixTrie = Trie()
                prefixTrie.insert(word)
                postfixTrie.insert(reverseMap[word])
                isPrefix = prefixTrie.searchWord(currWord)
                isPostFix = postfixTrie.searchWord(reversedCurrWord)
                if isPostFix and isPrefix:
                    count += 1

        return count