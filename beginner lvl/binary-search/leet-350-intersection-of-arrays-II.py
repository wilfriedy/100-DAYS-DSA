from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        def binSearch(target: int) -> bool:
            left, right = 0, len(nums1) - 1

            while left <= right:
                mid = (left + right) // 2
                midVal = nums1[mid]
                if midVal > target:
                    right = mid - 1
                elif midVal < target:
                    left = mid + 1
                else:
                    del nums1[mid]
                    return True
            return False

        result = []
        for num in nums2:
            if binSearch(num):
                result.append(num)
        return result