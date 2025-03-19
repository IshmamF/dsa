from collections import Counter
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        '''
        11001
        11
        1001000
        '''
        binNum2 = format(num2, 'b')
        binNum1 = format(num1, 'b')
        num2Sets = Counter(binNum2).get('1', 0)
        num1Sets = Counter(binNum1).get('1', 0)

        #print(binNum1, binNum2)

        if num2Sets == num1Sets:
            return num1
        elif num2Sets > len(binNum1):
            return int('1' * num2Sets, 2)
        
        ans = ['0'] * len(binNum1)
        
        for i, char in enumerate(binNum1):
            if num2Sets == 0:
                break
            elif char == '1':
                ans[i] = '1'
                num2Sets -= 1
        for i in range(len(ans)-1, -1, -1):
            if num2Sets == 0:
                break
            if ans[i] != '1':
                ans[i] = '1'
                num2Sets -= 1
        return int(''.join(ans), 2)