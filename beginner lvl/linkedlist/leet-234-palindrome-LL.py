# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        halfNode = slow
        prev = None

        while halfNode:
            nextNode = halfNode.next
            halfNode.next = prev
            prev = halfNode
            halfNode = nextNode

        reversedHalf = prev
        originalNode = head
        while reversedHalf:
            if reversedHalf.val != originalNode.val:
                return False
            reversedHalf = reversedHalf.next
            originalNode = originalNode.next

        return True
