num_tests = int(input())
tests = []
for _ in range(num_tests):
    t = input()
    tests.append(t)

def mirror(a):
    length = len(a)
    res = ''
    for i in range(length-1, -1, -1):
        c = a[i]
        if c=='p':
            res += 'q'
        elif c == 'q':
            res += 'p'
        else:
            res += c
    return res

for test in tests:
    print(mirror(test))