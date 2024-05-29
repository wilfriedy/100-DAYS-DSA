from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            mapPair = {}
            localTriplets = []

            for j in range(i + 1, len(nums)):
                third = -(target + nums[j])
                if third in mapPair:
                    foundTriplets = sorted([third, target, nums[j]])
                    if foundTriplets not in localTriplets:
                        localTriplets.append(foundTriplets)
                mapPair[nums[j]] = j
            print(localTriplets)
            triplets.extend(localTriplets)
        return triplets

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))