nums = [5,6,25,30]
nums.sort() # O(nlogn)
max_xor = 0
#O(n^2)
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
            current_max = nums[i] ^ nums[j]
            max_xor = max(max_xor, current_max)
        else:
            break
print(max_xor)