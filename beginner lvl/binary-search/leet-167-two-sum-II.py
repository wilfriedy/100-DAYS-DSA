from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = numbers[i] # possible first value
            y = target - x # new target and possible second value

            left = i + 1
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2

                if numbers[mid] > y:
                    right = mid - 1
                elif numbers[mid] < y:
                    left = mid + 1
                else:
                    return [i+1, mid+1]
        return []
