from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Count = Counter(nums1)
        nums2Count = Counter(nums2)
        result = []

        for num in nums1Count:
            if num in nums2Count:
                min_count = min(nums1Count[num], nums2Count[num])
                result.extend([num]*min_count)
        return result