class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def addItem(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        previousNode = self.head
        while previousNode.next is not None:
            previousNode = previousNode.next
        previousNode.next = new_node

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end="->")
            currentNode = currentNode.next
        # print(currentNode.data)


linkedListSolution = LinkedList()
linkedListSolution.addItem(2)
linkedListSolution.addItem(3)
linkedListSolution.addItem(5)
print(linkedListSolution.printLinkedList())
# print(linkedListSolution.head.data, end=f" -> next : {linkedListSolution.head.next.data}")
