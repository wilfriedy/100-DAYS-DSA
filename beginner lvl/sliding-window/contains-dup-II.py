from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distinctItemsMap = {}

        for i in range(len(nums)):
            print(distinctItemsMap)
            if nums[i] not in distinctItemsMap:
                distinctItemsMap[nums[i]] = i
            else:
                if abs(distinctItemsMap[nums[i]] - i) > k:
                    distinctItemsMap[nums[i]] = i
                else:
                    return True
        return False


solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))