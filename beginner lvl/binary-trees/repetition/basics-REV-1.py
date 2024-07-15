from typing import List


class Node:
    def __init__(self, val):
        self.value = val
        self.right = self.left = None

class BSTree:
    def __init__(self):
        self.root = None

    def insertNodes(self, val):
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if val < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            elif val > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right

def findValue(root:Node, value:int) -> Node | None:
    current_node = root

    while current_node:
        if current_node.value == value:
            return current_node
        if current_node.value > value:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return None


def preOrderTraversal(root: Node, result: List[int]):
    if root:
        result.append(root.value)
        preOrderTraversal(root.left, result)
        preOrderTraversal(root.right, result)




myTree = BSTree()
values = [4,2,7,3,1]
for value in values:
    myTree.insertNodes(value)

results = []
ans = findValue(myTree.root, 2)
preOrderTraversal(ans, results)

# preOrderTraversal(myTree.root, results)
#
print(results)
