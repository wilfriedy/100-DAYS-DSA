class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        elif not root2:
            return root1

        merged_tree = TreeNode(root1.val + root2.val)
        merged_tree.left = self.mergeTrees(root1.left, root2.left)
        merged_tree.right = self.mergeTrees(root1.right, root2.right)
        return merged_tree
