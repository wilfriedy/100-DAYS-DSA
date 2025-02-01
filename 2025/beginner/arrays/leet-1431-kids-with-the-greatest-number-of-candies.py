from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)
        result = []
        for num in candies:
            if (num + extraCandies >= maxNum):
                result.append(True)
            else:
                result.append(False)

        return result