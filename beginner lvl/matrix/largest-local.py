from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        maxLocal = [[0] * (N-2) for _ in range(N- 2)]
        for i in range(N-2):
            for j in range(N-2):
                for x in range(i, i+3):
                    for y in range(j, j + 3):
                        maxLocal[i][j] = max(grid[x][y], maxLocal[i][j])


        return maxLocal


solution = Solution()
print(solution.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))