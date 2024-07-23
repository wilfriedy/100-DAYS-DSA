from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        total_soldiers = [(sum(soldier), i) for i, soldier in enumerate(mat)]
        total_soldiers.sort(key= lambda sol_tup: sol_tup[0])
        return [row[1] for row in total_soldiers[:k]]

mySolution = Solution()
print(mySolution.kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]], 3))
