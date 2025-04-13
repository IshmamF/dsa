def find_output(k, l1, r1, l2, r2):
    count = 0
    for i in range(l1, r1 + 1):
        for j in range(i, r2 + 1):
            val = j / i 
            if k % val == 0:
                count += 1
    return count

num_tests = int(input())
output = []
for _ in range(num_tests):
    k, l1, r1, l2, r2 = map(int, input().split())
    output.append(find_output(k, l1, r1, l2, r2))

for val in output:
    print(val)