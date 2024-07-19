from typing import List

def binary_search(nums:List[int], target:int) -> bool:
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        mid_value = nums[middle]

        if mid_value > target:
            right = middle - 1
        elif mid_value < target:
            left = middle + 1
        else:
            return True
    return False

print(binary_search([1,2,3,4,5], 8))