from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        def check(a:int,b:int)-> int:
            inner_max = 0

            is_strong_pair = abs(nums[a] - nums[b]) <= min(nums[a], nums[b])
            if is_strong_pair:
                print((nums[a], nums[b]))
                inner_max = nums[a] ^ nums[b]
            return inner_max


        for i in range(len(nums)):
            for j in range(len(nums)):
                max_xor = max(max_xor, check(i, j))
        return max_xor

solution = Solution()
# print(solution.maximumStrongPairXor([1,2,3,4,5]))
# print(solution.maximumStrongPairXor([10,100]))
print(solution.maximumStrongPairXor([1,1,10,3,9]))