from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        count = 0

        for k in range(len(nums)):
            if nums[k] - diff in seen and nums[k] - 2*diff in seen:
                count +=1
            seen.add(nums[k])
