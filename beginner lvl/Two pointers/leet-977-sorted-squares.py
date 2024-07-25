from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        res = [0]*n
        indx = n-1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[indx] = nums[right]**2
                right -= 1
            else:
                res[indx] = nums[left]**2
                left +=1
            indx -= 1

        return res
