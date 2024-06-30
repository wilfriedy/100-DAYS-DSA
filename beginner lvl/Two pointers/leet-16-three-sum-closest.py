from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort nums
        nums.sort()
        closest_sum = float("inf")
        for i in range(len(nums) - 2):
            left = i +1
            right = len(nums) -1
            while left < right:
                current_closest = nums[i] + nums[left] + nums[right]
                if abs(current_closest - target) < abs(closest_sum - target):
                    closest_sum = current_closest

                if target < current_closest:
                    right -= 1
                elif target > current_closest:
                    left += 1
                else:
                    return current_closest

        return closest_sum


solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1))

