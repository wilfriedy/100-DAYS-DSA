# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the nodes after the middle
        prev = None
        currentNode = slow.next
        slow.next = None #divides the list into two

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode

        secondHalfReversed = prev
        first = head # the head has been modified to contain every node up to the slow pointer i.e halved

        while secondHalfReversed:
            # set 2 temp nodes to hold the next node in each half
            temp1 = first.next
            temp2 = secondHalfReversed.next

            first.next = secondHalfReversed
            secondHalfReversed.next = temp1

            first = temp1
            secondHalfReversed = temp2



