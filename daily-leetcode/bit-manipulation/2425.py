class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        nums1
        0010
        0001
        0011
        0011
        0000

        nums2
        1010
        0010
        1000
        0101
        0000
        1101

        2 with every comb of num2
        1000 <- 0010 & 1010
        0000 <- 0010 & 0010
        1000
        0111 <- 0010 & 0101
        1111
        0010 <- 0010 & 0000
        1101

        1 with every comb of num2
        1101
        1011 <- 0001 & 1010
        0110
        0011 <- 0001 & 0010
        0101
        0100 <- 0001 & 0101
        0001
        0001 <- 0001 & 0000
        0000
        3 with every comb of num2
        1001 <- 0011 & 1010
        0001 <- 0011 & 0010
        1000
        0110 <- 0011 & 0101
        1110
        0011 <- 0011 & 0000
        1101

        nums1 <- 0001 & 0010
        nums2 <- 0011 & 0100

        0010 1 & 3 = 2
        0101 1 & 4 = 5
        0111 7
        0001 2 & 3 = 1
        0110 6
        0110 2 & 4 = 6
        0000 0

        1011001 <- 89
        0001011 <- 11
        1010010 <- 82

        0010 <- 2
        1011 <- 11
        1001 <- 9

        01001 <- 9
        11000 <- 24
        10001
        '''
        xorOfNums1 = 0
        for n1 in nums1:
            xorOfNums1 = xorOfNums1 ^ n1
        print(xorOfNums1)
        xorOfNums2 = 0
        for n2 in nums2:
            xorOfNums2 = xorOfNums2 ^ n2
        print(xorOfNums2)
        if len(nums2) % 2 == 0 and len(nums1) % 2 == 0:
            return 0
        elif len(nums2) % 2 == 1 and len(nums1) % 2 == 1:
            return xorOfNums1 ^ xorOfNums2
        elif len(nums2) % 2 == 0:
            return xorOfNums2
        else:
            return xorOfNums1