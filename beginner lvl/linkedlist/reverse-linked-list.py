# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        prev = None
        while currentNode is not None:
            nextValue = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextValue
        return prev