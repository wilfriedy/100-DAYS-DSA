class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middleNode = slow
        prev = None

        while middleNode:
            nextNode = middleNode.next
            middleNode.next = prev
            prev = middleNode
            middleNode = nextNode

        reversedHalfNode = prev
        originalNode = head
        maxSum = 0
        while reversedHalfNode:
            localSum = reversedHalfNode.val + originalNode.val
            maxSum = max(maxSum, localSum)
            reversedHalfNode = reversedHalfNode.next
            originalNode = originalNode.next
        return maxSum