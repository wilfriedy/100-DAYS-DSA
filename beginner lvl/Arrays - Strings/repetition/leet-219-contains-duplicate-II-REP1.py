from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict = {}
        for i, val in enumerate(nums):
            if val not in myDict:
                myDict[val] = i
            else:
                j = myDict[val]
                if abs(i - j) <= k:
                    return True
                else:
                    myDict[val] = i
        return False


