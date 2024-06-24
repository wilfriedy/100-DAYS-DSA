# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head.next:
            return
        slow = fast = head
        prev_slow = None # keeps track of the preceding nodes of slow

        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next

        #redirect the next pointer of prev_slow to the node after slow to delete the middle node
        while prev_slow:
            prev_slow.next = slow.next

        return head