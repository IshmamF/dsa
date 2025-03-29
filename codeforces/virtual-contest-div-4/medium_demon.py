def find_num_exchanges(size, spider_give):
    old = [1] * size
    num_exchanges = 1
    while True:
        temp = old.copy()
        for i, index in enumerate(spider_give):
            if temp[i] > 0:
                temp[i] -= 1
                temp[index - 1] += 1
        for i in range(size):
            if temp[i] > 1:
                temp[i] = 1
        num_exchanges += 1
        if temp == old:
            break
        old, temp = temp, old
    return num_exchanges

    
num_tests = int(input())
res = []
for _ in range(num_tests):
    size = int(input())
    spider_give = list(map(int, input().split()))
    res.append(find_num_exchanges(size, spider_give))
for val in res:
    print(val)