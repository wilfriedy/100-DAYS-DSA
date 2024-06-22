from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        count = 0
        prod = 1

        for right, num in enumerate(nums):
            prod *= num

            while prod >= k:
                prod //= nums[left]
                left += 1

            count += right - left + 1
        return count


solution = Solution()
print(solution.numSubarrayProductLessThanK([10,5,2,6], 100))
# print(solution.numSubarrayProductLessThanK([1,2,3], 0))
# print(solution.numSubarrayProductLessThanK([1,1,1], 2))




