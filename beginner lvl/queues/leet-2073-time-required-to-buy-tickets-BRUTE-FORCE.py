from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    return time
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
        return time

sol = Solution()
print(sol.timeRequiredToBuy([2,3,2], 2))