from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        hashmap = {}

        groupCount = 0
        for num in sorted(nums):
            if not groups:
                q = deque([num])
                groups.append(q)
            elif num - groups[-1][-1] <= limit:
                groups[-1].append(num)
            else:
                q = deque([num])
                groups.append(q)
                groupCount += 1
            hashmap[num] = groupCount

        for i,num in enumerate(nums):
            groupNum = hashmap[num]
            swapNum = groups[groupNum].popleft()
            nums[i] = swapNum

        return nums