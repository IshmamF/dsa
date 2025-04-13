n, k = map(int, input().split())
planks = list(map(int, input().split()))



l = 0
minSoFar = float('inf')
minLeftPtr = 0
totalSoFar = 0
for r in range(n):
    totalSoFar += planks[r]

    if r - l + 1 == k:
        if totalSoFar < minSoFar:
            minSoFar = totalSoFar
            minLeftPtr = l

        totalSoFar -= planks[l]
        l += 1
    
print(minLeftPtr+1)
