def find_max(m, a, b, c):
    num_seats = m * 2
    res = 0
    '''
    10 5 5 10
    3 6 1 1
    15 14 12 4
    1 1 1 1
    420 6 9 69
    '''

    if a > m:
        res += m
    elif a <= m:
        res += a

    if b > m:
        res += m
    elif b <= m:
        res += b

    if res >= num_seats:
        return res
    else:
        if res + c <= num_seats:
            return res + c
        else:
            res += num_seats - res
            return res
    
num_tests = int(input())
output = []
for _ in range(num_tests):
    m, a, b, c = map(int, input().split())
    output.append(find_max(m, a, b, c))

for val in output:
    print(val)
