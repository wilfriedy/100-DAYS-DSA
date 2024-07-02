from collections import deque
nums = [1,2,3,5]
newQueue = deque(nums)
newQueue.append(newQueue.popleft())
print(newQueue)
# nums.append(nums.pop(0))
# print(nums)
# nums.remove(3)
# print(nums)