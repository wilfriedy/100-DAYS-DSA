from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        x,y = 0, n

        while x < n:
            shuffled.append(nums[x])
            shuffled.append(nums[y])
            x += 1
            y += 1
        return shuffled

solTest = Solution().shuffle([2,5,1,3,4,7], 3)

print(solTest)
