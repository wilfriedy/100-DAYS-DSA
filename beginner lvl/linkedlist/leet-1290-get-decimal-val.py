# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current_node = head
        node_values = ''
        while current_node:
            node_values = node_values + str(current_node.val)
            current_node = current_node.next

        return int(node_values)

n1 = ListNode(1)
n1.next = ListNode(3)

mySolution = Solution()
print(mySolution.getDecimalValue(n1))