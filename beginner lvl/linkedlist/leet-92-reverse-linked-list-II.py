class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if right == left:
            return head

        fakeNode = ListNode(0, head)
        nodeBeforeLeft = fakeNode
        for _ in range(left-1):
            nodeBeforeLeft = nodeBeforeLeft.next

        nodeAtLeft = nodeBeforeLeft.next

        for _ in range(right - left):
            temp = nodeAtLeft.next
            nodeAtLeft.next = temp.next
            temp.next = nodeBeforeLeft.next
            nodeBeforeLeft.next = temp

        return fakeNode.next
