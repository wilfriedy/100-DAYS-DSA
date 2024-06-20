# step 1 determine if the linked list has a cycle
# step 2 get node where the cycle began
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return slow
        return None


