from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        endIndx1 = m -1
        endIndx2 = n -1
        lastItemInFinalNums1Index = m + n -1

        while endIndx2 >= 0:
            if endIndx1 >= 0 and nums1[endIndx1] > nums2[endIndx2]:
                nums1[lastItemInFinalNums1Index] = nums1[endIndx1]
                endIndx1 -= 1
            else:
                nums1[lastItemInFinalNums1Index] = nums2[endIndx2]
                endIndx2 -= 1
            lastItemInFinalNums1Index -= 1