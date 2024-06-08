from typing import List


def maxSubArraySum(nums:List, k:int):
    maxSum = copySum = sum(nums[:k])

    for i in range(len(nums) - k):
        copySum -= nums[i]
        copySum += nums[i + k]
        maxSum = max(maxSum, copySum)
    return maxSum
nums = [1,2,6,2,4,1]

print(maxSubArraySum([3,5,6,8], 2))