class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = new_node

    def printNodes(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end="->")
            currentNode = currentNode.next

def mergeTwoLinkedList(list1, list2):
    placeholderNode = Node(0)
    copiedNode = placeholderNode

    while list1 and list2:
        if list1.data < list2.data:
            copiedNode.next = list1
            list1 = list1.next
        else:
            copiedNode.next = list2
            list2 = list2.next
        copiedNode = copiedNode.next

    if list1 is not None:
        copiedNode.next = list1
    if list2 is not None:
        copiedNode.next = list2
    return placeholderNode.next


def printLL(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.data, end="->")
        currentNode = currentNode.next

list1 = LinkedList()
list1.addNode(1)
list1.addNode(2)
list1.addNode(4)
list1.addNode(11)
list1.printNodes()
print('')
list2 = LinkedList()
list2.addNode(1)
list2.addNode(3)
list2.addNode(4)
list2.addNode(44)
list2.addNode(70)
list2.printNodes()
print('')
merged = mergeTwoLinkedList(list1.head, list2.head)
printLL(merged)
