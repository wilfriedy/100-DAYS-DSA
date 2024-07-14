from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        i, j = 0, len(nums)-1

        while i < j:
            total = nums[i] + nums[j]

            if total > target or total == target:
                j -=1
            else:
                count += j - i
                i += 1
        return count

mySolution = Solution()
print(mySolution.countPairs([-1,1,2,3,1], 2))
