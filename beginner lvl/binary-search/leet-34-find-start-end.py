from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft():
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return first

        def searchRight():
            left, right = 0, len(nums) - 1
            second = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    second = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return second

        firstPoint = searchLeft()
        if firstPoint == -1:
            return [-1, -1]
        secondPoint = searchRight()
        return [firstPoint, secondPoint]