class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_set = set()
        current_node = headA

        while current_node:
            nodes_set.add(current_node)
            current_node = current_node.next

        current_node = headB

        while current_node:
            if current_node in nodes_set:
                return current_node
            current_node = current_node.next

        return None
