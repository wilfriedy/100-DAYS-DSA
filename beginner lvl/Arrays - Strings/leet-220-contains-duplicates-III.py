from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        myDict = {}
        for i, val in enumerate(nums):
            if val not in myDict:
                myDict[val] = i
            else:
                j = myDict[val]

                if abs(i - j) <= indexDiff and abs(val - nums[j]) <= valueDiff:
                    return True
                else:
                    myDict[val] = i
        return False

mySol = Solution()
print(mySol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))