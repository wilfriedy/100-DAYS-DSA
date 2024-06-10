class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None


class Dlist:
    def __init__(self):
        self.head = None

    def addNode(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next
        new_node.prev = currentNode
        currentNode.next = new_node

    def prepend(self, val):
        new_node = Node(val)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.val, end="->")
            currentNode = currentNode.next
    def reverseList(self):
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        while currentNode:
            print(currentNode.val, end="->")
            currentNode = currentNode.prev


NdList = Dlist()
NdList.addNode(2)
NdList.addNode(3)
NdList.addNode(4)
NdList.printList()
print("")
NdList.reverseList()