from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]
                if total < target:
                    count += 1
        return count


mySolution = Solution()
nums = [-1,1,2,3,1]
target = 2
print(mySolution.countPairs(nums, target))