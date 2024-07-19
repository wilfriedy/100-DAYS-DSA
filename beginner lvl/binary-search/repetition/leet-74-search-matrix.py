from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) # length of the rows in the matrix / number of columns
        m = len(matrix) # size of the matrix
        left = 0
        right = (m * n) - 1

        while left <= right:
            middle = (left + right) // 2
            mid_val = matrix[middle // n][middle % n] #get row and column at which the middle is

            if mid_val > target:
                right = middle - 1
            elif mid_val < target:
                left = middle + 1
            else:
                return True
        return False
