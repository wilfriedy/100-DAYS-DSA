# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode):
        prev = None
        current_node = head

        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        return prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        carry = 0
        fake_node = ListNode()
        current_node = fake_node

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            new_node = ListNode(total % 10)
            current_node.next = new_node
            current_node = current_node.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return self.reverseList(fake_node.next)
