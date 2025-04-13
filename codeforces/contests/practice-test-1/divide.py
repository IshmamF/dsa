n = input()
digits = [d for d in n]
size = len(digits)

def isDivisible(digits, size):
    memo = {}
    def helper(i, num, size):
        if (i, num) in memo:
            return memo[(i, num)]
        if i == size:
            return num if num != '' and int(num) % 8 == 0 else ''
        if num != '' and int(num) % 8 == 0:
            return num
        
        include = helper(i + 1, num + digits[i], size)
        dontInclude = helper(i+1, num, size)
        if include != '':
            memo[(i, num)] = include
            return include
        elif dontInclude != '':
            memo[(i, num)] = dontInclude
            return dontInclude
        else:
            memo[(i, num)] = ''
            return ''
    val = helper(0, "", size)
    if val == '':
        print('NO')
    else:
        print('YES')
        print(val)

isDivisible(digits, size)  
