# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current_node = root
        while current_node:
            if val == current_node.val:
                return current_node
            if val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None