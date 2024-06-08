from typing import List

def subArraySum(N:List, k:int) -> int:
    max_sum = inner_max = sum(N[:k])

    for i in range(len(N) - k):
        inner_max += N[i + k] - N[i]
        max_sum = max(max_sum, inner_max)
    return max_sum

print(subArraySum([1,2,6,2,4,1], 3))
