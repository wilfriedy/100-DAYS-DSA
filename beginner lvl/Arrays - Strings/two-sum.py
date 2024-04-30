from typing import List
# nums = [2,7,11,15], target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapX = {}

        for i in range(len(nums)):
            mapX[nums[i]] = i
        for i in range(len(nums)):
            ny = target - nums[i]
            if ny in mapX and mapX[ny] != i:
                return [mapX[ny], i]
        # print(mapX)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


solution = Solution()
print(solution.twoSum([7,11,2,15], 9))