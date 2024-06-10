class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class DblyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode

    def printNodes(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end="->")
            currentNode = currentNode.next

    def prependNode(self, value):
        newNode = Node(value)
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def reverseDlist(self):
        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next

        while currentNode:
            print(currentNode.value, end="->")
            currentNode = currentNode.prev




Dlist = DblyLinkedList()
numList = [2,4,3,6]
for num in numList:
    Dlist.addNode(num)

Dlist.prependNode(100)
Dlist.printNodes()
print("")
Dlist.reverseDlist()