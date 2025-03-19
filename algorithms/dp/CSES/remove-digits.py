from typing import List
def removingDigits(num:int) -> int:
    '''
    Wouldn't we just choose the biggest number each time from all digits?
    We need to get each digit, and one way to do so is through modulo operation
    I'm assuming this approach is pretty slow
    but wouldn't you have to break the number into separate digits anyways?
    '''
    def convert_int_to_list(input: int) -> int:
        maxDigit = -1
        while input > 9:
            rightMost = input % 10 
            maxDigit = max(maxDigit, rightMost)
            input = input // 10
        maxDigit = max(maxDigit, input)
        return maxDigit

    def recurse(curr_digit: int) -> int:
        if curr_digit == 0:
            return 0 
        
        maxDigit = convert_int_to_list(curr_digit)
        return 1 + recurse(curr_digit-maxDigit)
    
    return recurse(num)

val = removingDigits(123)   
print(val)