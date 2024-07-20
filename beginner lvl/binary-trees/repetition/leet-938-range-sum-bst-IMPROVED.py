class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    if root is None:
        return 0
    sum_of_nodes = 0

    if low <= root.val <= high:
        sum_of_nodes += root.val
        if low < root.val:
            sum_of_nodes += rangeSumBST(root.left, low, high)
        if high > root.val:
            sum_of_nodes += rangeSumBST(root.right, low, high)

    return sum_of_nodes


