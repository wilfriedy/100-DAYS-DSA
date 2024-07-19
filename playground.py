# from typing import List
#
ints = [1,2,3,4,5]
print(ints[69 % len(ints)])
print(5%4)



# def bin_search(nums:List[int], target:int) -> bool:
#     nums.sort()
#     left = 0
#     right = len(nums) -1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if target < nums[mid]:
#             right = mid - 1
#         elif target > nums[mid]:
#             left = mid + 1
#         else:
#             return True
#     return False
#
# print(bin_search(ints, 3))



