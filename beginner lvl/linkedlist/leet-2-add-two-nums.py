# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        retained = 0
        current_node = dummy_node

        while l1 or l2 or retained:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + retained
            retained = total // 10

            new_node = ListNode(total % 10)
            current_node.next = new_node
            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_node.next
