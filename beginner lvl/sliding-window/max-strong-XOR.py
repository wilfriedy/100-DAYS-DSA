from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        sorted_num = nums.sort()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    current_max = nums[i] ^ nums[j]
                    max_xor = max(max_xor, current_max)
                else:
                    break
        return max_xor

solution = Solution()
print(solution.maximumStrongPairXor([1,2,3,4,5]))
# print(solution.maximumStrongPairXor([10,100]))
# print(solution.maximumStrongPairXor([1,1,10,3,9]))