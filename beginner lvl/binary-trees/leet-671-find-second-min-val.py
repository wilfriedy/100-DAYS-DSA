class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    class Solution:
        def __init__(self):
            self.second_minimum = None
            self.first_min = None
            self.found = False

        def findSecondMinimumValue(self, root: TreeNode) -> int:

            self.first_min = root.val
            self.second_minimum = float('inf')
            self.found = False

            def dfs(node: TreeNode):
                if not node:
                    return
                if self.first_min < node.val < self.second_minimum:
                    self.second_minimum = node.val
                    self.found = True
                dfs(node.left)
                dfs(node.right)

            dfs(root)

            return self.second_minimum if self.second_minimum < float('inf') else -1
            # return self.second_minimum if self.found else -1