from typing import List

def insertAtIndex(idx:int, value:int, nums:List[int]):
    if idx < 0 or idx > len(nums):
        print("Out of range")
    nums.append(0)
    print(nums)
    for i in range(len(nums)-1, idx, -1):
        nums[i] = nums[i-1]
    print(nums, "after shifting")
    nums[idx] = value
    return nums

newList = insertAtIndex(4, 5, [1,2,3,4,6])