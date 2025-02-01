from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i, count = 0, 0

        while i < len(nums):
            j = len(nums) - 1
            while j > i:
                if (nums[i] == nums[j]):
                    count += 1
                j -= 1

            i += 1

        return count

solTest = Solution().numIdenticalPairs([1,2,3,1,1,3])
print(solTest)
