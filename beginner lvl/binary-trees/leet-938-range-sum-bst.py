# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preOrderTrav(self, node: TreeNode, low: int, high: int, sum_nodes:List[int]):
        if node:
            if low <= node.val <= high:
                sum_nodes[0] += node.val
            self.preOrderTrav(node.left, low, high, sum_nodes)
            self.preOrderTrav(node.right, low, high, sum_nodes)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = []
        self.preOrderTrav(root, low, high, total)
        return total[0]

