from typing import List


def appendToTop(value:int, nums:List[int]):
    nums.append(value)
    for i in range(len(nums) - 1):
        nums.append(nums.pop(0))