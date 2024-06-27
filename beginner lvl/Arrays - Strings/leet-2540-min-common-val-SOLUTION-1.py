from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binSearch(target:int) -> bool:
            left = 0
            right = len(nums1) -1
            while left <= right:
                mid = (left + right)//2
                midVal = nums1[mid]

                if midVal > target :
                    right = mid -1
                elif midVal < target:
                    left = mid +1
                else:
                    return True
            return False

        for num in nums2:
            if binSearch(num):
                return num
        return -1





