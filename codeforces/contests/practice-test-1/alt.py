def calcMaxSub(n, seq):
    maxSum = []
    maxLen = 0
    for i in range(n):
        currSum = seq[i]
        currLen = 1
        prevIsPos = seq[i] > 0
        for j in range(i+1, n):
            if (prevIsPos and seq[j] < 0) or (not prevIsPos and seq[j] > 0):
                currSum += seq[j]
                currLen += 1
                prevIsPos = not prevIsPos
                if currLen >= maxLen:
                    maxSum.append(currSum)
                    maxLen = currLen
    return max(maxSum) if maxSum else -1

t = int(input())

res = []
for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    val = calcMaxSub(n, seq)
    print(val)
