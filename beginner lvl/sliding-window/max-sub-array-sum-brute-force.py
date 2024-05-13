from typing import List

def subArraySum(N:List, k:int) -> int:
    max_sum = 0

    for left in range(len(N) - k +1):
        inner_max = N[left]
        for j in range(1, k):
            right = left+j
            inner_max += N[right]
        max_sum = max(max_sum, inner_max)

    return max_sum

print(subArraySum([1,2,6,2,4,1], 3))