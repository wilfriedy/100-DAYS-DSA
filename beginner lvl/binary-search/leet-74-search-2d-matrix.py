from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            currentRow = matrix[i]
            left, right = 0, len(currentRow) -1
            if currentRow[left] <= target <= currentRow[right]:
                while left <= right:
                    mid = (left + right) // 2
                    if currentRow[mid] > target:
                        right = mid -1
                    elif currentRow[mid] < target:
                        left = mid + 1
                    else:
                        return True
            else:
                continue

        return False
