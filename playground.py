class Node:
    def __init__(self, value):
        self.data = value
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

def reverseLinkedList(linkedListHead):
    currentNode = linkedListHead
    prev = None
    while currentNode is not None:
        nextValue = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = nextValue
    return prev

def getMiddle(head:Node)->Node:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def printLL(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.data, end="->")
        currentNode = currentNode.next

myLinkedList = LinkedList()
nums = [1,2,3,4]
for num in nums:
    myLinkedList.addItem(num)

myLinkedList.printLinkedList()
midNode = getMiddle(myLinkedList.head)
print("")
printLL(midNode)