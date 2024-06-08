
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxLen = 0
        char_count = {}
        left = 0

        for right in range(len(nums)):
            if nums[right] in char_count:
                char_count[nums[right]] += 1
            else:
                char_count[nums[right]] = 1

            while char_count[nums[right]] > k:
                char_count[nums[left]] -= 1
                if char_count[nums[left]] == 0:
                    del char_count[nums[left]]
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen
