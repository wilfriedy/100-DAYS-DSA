from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            total = nums[i] + nums[j]
            if total > target or total == target:
                j -= 1
            else:
                count += j - i
                i += 1

        return count

mySolution = Solution()
nums = [-1,1,2,3,1]
target = 2
print(mySolution.countPairs(nums, target))