n = int(input())
costs = list(map(int, input().split()))
q = int(input())
coins = []
for i in range(q):
    coins.append([int(input()), i])


costs.sort()
coins.sort()

index = 0
res = [0] * q
passed = 0
for coin, coin_index in coins:
    for i in range(index, n):
        if coin < costs[i]:
            index = i
            break
        passed += 1
    res[coin_index] = passed
for val in res:
    print(val)