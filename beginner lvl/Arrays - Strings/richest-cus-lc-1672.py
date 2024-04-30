from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in range(len(accounts)):
            currentRichest = 0
            for j in range(len(accounts[i])):
                currentRichest += accounts[i][j]
            if currentRichest > richest:
                richest = currentRichest

        return richest

solution = Solution()
print(solution.maximumWealth([[1,5],[7,3],[3,5]]))