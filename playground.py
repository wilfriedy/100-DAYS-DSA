class Node:
    def __init__(self, value):
        self.val = value
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

def printList(head:Node):
    currentNode = head
    while currentNode:
        print(currentNode.val, end="->")
        currentNode = currentNode.next

def reverseLinkedList(head:Node):
    currentNode = head
    prev = None
    # while currentNode
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = nextNode
    return prev

def getMiddle(head:Node):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

newList = LinkedList()
newList.addNode(1)
newList.addNode(2)
newList.addNode(3)
# newList.addNode(4)
printList(newList.head)
reversedList = reverseLinkedList(newList.head)
print('')
printList(reversedList)
print("")
middleNode = getMiddle(newList.head)
printList(middleNode)
