from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashTable = {}
        for i in nums:
            if i not in hashTable:
                hashTable[i] = 1
            else:
                hashTable[i] += 1
        for j in hashTable:
            if hashTable[j] == 1:
                return j