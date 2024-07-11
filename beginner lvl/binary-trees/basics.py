from collections import deque


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BinaryTree :
    def __init__(self):
        self.root = None

    def insertNode(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)


myTree = BinaryTree()
# values = [100,101,99,97,86,140,120,44]
values = [10,2,11,23,4,5,15]
for value in values:
    myTree.insertNode(value)

preorder_result = []
myTree.preorder_traversal(myTree.root, preorder_result)
print("Preorder Traversal:", preorder_result)