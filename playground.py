from typing import List


class Node :
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None

class MyTree:
    def __init__(self):
        self.root = None

    def insertNode(self, val):
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
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right

def preOrderTraversal(node:Node):
    if node:
        # result.append(node.value)
        print(node.value)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

values = [10,2,11,23,4,5,15]
mytree = MyTree()
for value in values:
    mytree.insertNode(value)

preOrderTraversal(mytree.root)
