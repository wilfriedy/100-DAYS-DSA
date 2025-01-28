from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsOfZeros = 0
        while 0 in nums:
            nums.remove(0)
            numsOfZeros +=1

        nums.extend([0] * numsOfZeros)