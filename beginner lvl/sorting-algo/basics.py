# selection sort implementation
from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(n - 1):
        current_min = i
        for j in range(i + 1, n):
            if nums[current_min] > nums[j]:
                current_min = j

        nums[i], nums[current_min] = nums[current_min], nums[i]

    return nums

print(selection_sort([66,8,100,1,3,0]))