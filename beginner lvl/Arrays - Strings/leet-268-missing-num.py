from typing import List


class Solution:
    # optimised version
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumOfAllNumsInrange = (n*(n+1))//2
        return sumOfAllNumsInrange - sum(nums)
    # def missingNumber(self, nums: List[int]) -> int:
    #     numsRange = set(range(len(nums)+1))
    #     for num in nums:
    #         numsRange.remove(num)
    #     return numsRange.pop()


solution = Solution()
print(solution.missingNumber([3,0,1]))