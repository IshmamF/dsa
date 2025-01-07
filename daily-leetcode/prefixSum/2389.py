'''
index range:
0 to 1 : backward so -1
1 to 2 : forward so +1
0 to 2 : forward so +1

index:
0 <- move 0 characters
1 <- move 1 character
2 <- move 2 characters 

for index, we can use hashmap to map index to how many characters we have to move
we would need to adjust it if it's below 97 and above 122 , we can prob use modulo for this

'''

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_list = list(s)

        prefix = [0] * (len(s) + 1)
        for shift in shifts:
            start, end, direction = shift
            direction = -1 if direction == 0 else 1
            prefix[start] += -direction
            prefix[end + 1] += direction
        
        currentPrefix = prefix[-1]
        for i in range(len(s)-1, -1, -1):
            char_ascii = ord(s[i])
            new_ascii = char_ascii + currentPrefix

            if new_ascii < ord('a'):
                new_ascii = (ord('a') - new_ascii - 1) % 26
                new_ascii = ord('z') - new_ascii
            elif new_ascii > ord('z'):
                new_ascii = ((new_ascii - ord('z') - 1) % 26)
                new_ascii += ord('a')
            s_list[i] = chr(new_ascii)
            currentPrefix += prefix[i]
        

        return "".join(s_list)
