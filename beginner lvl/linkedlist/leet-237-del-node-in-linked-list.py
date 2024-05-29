class Solution:
    def deleteNode(self, node):
        # nodeCopy = node
        node.val = node.next.value
        node.next = node.next.next