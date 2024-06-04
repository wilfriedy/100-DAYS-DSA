from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n-1
        while left <= right:
            mid = (left + right) // 2
            midValue = matrix[mid // n][mid % n]

            if midValue > target:
                right = mid - 1
            elif midValue < target:
                left = mid + 1
            else:
                return True
        return False

solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))