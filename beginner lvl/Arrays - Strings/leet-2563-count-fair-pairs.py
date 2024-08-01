from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0
        while i < j:
            total = nums[i] + nums[j]

            if total > upper:
                j -= 1
            elif total < lower:
                i += 1
            elif lower <= total <= upper:
                count += j - i
                i += 1

        return count