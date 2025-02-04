from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        idx = n - 1
        result = [0]*n

        while left <= right:
            if(abs(nums[left]) > abs(nums[right])):
                result[idx] = nums[left]**2
                left += 1
            else:
                result[idx] = nums[right]**2
                right -= 1
            idx -= 1
        return result

sol = Solution().sortedSquares([-4,-1,0,3,10])
print(sol)