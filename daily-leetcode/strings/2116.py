class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        '''
        "))()))" "010100"
        total, open, close
        initial : 5, 0, 0
        5, 0, 1 -> 3, 1, 0
        3, 1, 1
        2, 2, 1
        2, 2, 2
        2, 2, 3 -> 0, 3, 2
        0, 3, 3

        "())("
        total, open, close
        initial : 2, 0, 0
        1, 1, 0
        1, 1, 1
        1, 1, 2 -> 0, 2, 1
        0, 2, 1 -> 0, 2, 2

        "()()" "0000"
        total, open, close
        initial : 2, 0, 0
        1, 1, 0
        1, 1, 1
        0, 2, 1
        0, 2, 2

        ')' '0'
        total, open, close
        initial : 1, 0, 0
        1, 0, 1 -> -1, 1, 0

        ")("
        total, open, close
        initial: 1, 0, 0
        1, 0, 1 -> -1, 1, 0
        -1, 1, 0 -> 0, 1, 1
        '''
        if len(s) % 2 != 0:
            return False

        # Forward pass, checks open >= closed
        openParen, closedParen, numChanges = 0, 0, 0
        for i, c in enumerate(s):
            if locked[i] == '1':
                if c == '(':
                    openParen += 1
                else:
                    closedParen += 1
            else:
                numChanges += 1 

            if closedParen > openParen + numChanges:
                return False

        # Backward pass, checks closed >= open
        openParen, closedParen, numChanges = 0, 0, 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if locked[i] == '1':
                if c == '(':
                    openParen += 1
                else:
                    closedParen += 1
            else:
                numChanges += 1 

            if openParen > closedParen + numChanges:
                return False
        
        return True 