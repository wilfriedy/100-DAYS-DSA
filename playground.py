from typing import List
from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numsCount = Counter(nums)
        for num in numsCount:
            if numsCount[num] > 1:
                return num


solution = Solution()
print(solution.findDuplicate([1,3,4,2,2]))