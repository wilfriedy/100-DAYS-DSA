from typing import List
from collections import Counter

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        tracker = Counter(nums[0])
        for i in range(1, len(nums)):
            currentCount = Counter(nums[i])
            for num in tracker:
                if num not in currentCount:
                    tracker[num] = 0
        result = []
        for num, count in tracker.items():
            if count > 0:
                result.append(num)
        print(result)
        result.sort()
        return result


solution = Solution()
print(solution.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))


