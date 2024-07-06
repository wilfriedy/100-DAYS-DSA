from typing import List


class Solution:
    def containsDuplicateSecApproach(self, nums: List[int]) -> bool:
        myDict = {}
        for num in nums:
            if num not in myDict:
                myDict[num] = 1
            else:
                myDict[num] += 1
                if myDict[num] > 1:
                    return True
        return False
    def containsDuplicate(self, nums: List[int]) -> bool:
        int_set = set()

        for num in nums:
            if num not in int_set:
                int_set.add(num)
            else:
                return True
        return False

mySol = Solution()
print(mySol.containsDuplicateSecApproach([1,2,3,1]))