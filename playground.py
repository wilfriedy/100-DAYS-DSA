from typing import List

nums = [1,2,3,4]
def insertValueInFrontOfArray(array:[List], value, position):
    array.append('_')
    print(array)
    for i in range(len(array)-1, position, -1):
        array[i] = array[i-1]
    array[position] = value
    print(array)

insertValueInFrontOfArray(nums, 5, 2)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None