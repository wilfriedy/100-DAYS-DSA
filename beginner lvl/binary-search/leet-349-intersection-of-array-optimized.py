from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        result = set()
        def binSearch(target):
            left, right = 0, len(nums1) -1
            while left <= right:
                mid = (left + right) // 2
                midValue = nums1[mid]

                if midValue > target:
                    right = mid - 1
                elif midValue < target:
                    left = mid + 1
                else:
                    return True
            return False

        for num in nums2:
            if binSearch(num):
                result.add(num)

        return list(result)



