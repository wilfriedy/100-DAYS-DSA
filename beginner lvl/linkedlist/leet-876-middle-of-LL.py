class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = new_node
    
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end="->")
            currentNode = currentNode.next

def middleNode(head):
    listSize = 0
    currentNode = head

    while currentNode:
        listSize +=1
        currentNode = currentNode.next

    middle = listSize // 2
    middleNode = head
    for _ in range(1, middle):
        middleNode = middleNode.next

    return middleNode.next

def printLL(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.data, end="->")
        currentNode = currentNode.next

linkedListSolution = LinkedList()
linkedListSolution.addNode(1)
linkedListSolution.addNode(2)
linkedListSolution.addNode(3)
linkedListSolution.addNode(4)
linkedListSolution.addNode(5)
linkedListSolution.addNode(6)
print(linkedListSolution.printLinkedList())
middle = middleNode(linkedListSolution.head)
printLL(middle)