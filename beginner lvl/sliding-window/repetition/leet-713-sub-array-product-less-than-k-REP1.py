from typing import List

nums = [10, 5, 2, 6]
k = 100
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        prod = 1
        count = 0
        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1
        return count

solution = Solution()
print(solution.numSubarrayProductLessThanK(nums, k))
