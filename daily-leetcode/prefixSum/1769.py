class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        res = list(boxes)
        balls = 0
        moves = 0

        for i in range(len(boxes)):
            res[i] = balls + moves
            moves = balls + moves
            balls += int(boxes[i])
        
        balls = 0
        moves = 0

        for i in range(len(boxes)-1, -1, -1):
            res[i] += balls + moves
            moves = balls + moves
            balls += int(boxes[i])

        return res
