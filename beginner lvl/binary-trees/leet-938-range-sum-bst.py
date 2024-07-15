# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preOrderTrav(self, node: TreeNode, low: int, high: int, sum_nodes:int):
        if node:
            if low <= node.val <= high:
                sum_nodes += node.val
            self.preOrderTrav(node.left, low, high, sum_nodes)
            self.preOrderTrav(node.right, low, high, sum_nodes)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        self.preOrderTrav(root, low, high, total)
        return total

