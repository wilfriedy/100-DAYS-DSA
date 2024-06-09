class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
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

def getPositionByValue(head:Node, value):
    position = 1
    currentNode = head
    while currentNode:
        if currentNode.val == value:
            return position
        currentNode = currentNode.next
        position +=1
    return -1

def deleteDuplicates(head:Node):
    currentNode = head
    while currentNode.next:
        if currentNode.val == currentNode.next.val:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next
    return head

def printList(head:Node):
    currentNode = head
    while currentNode:
        print(currentNode.val, end="->")
        currentNode = currentNode.next

List = LinkedList()
nodes = [1,2,2,4]
for nums in nodes:
    List.addNode(nums)

printList(List.head)
print('')
newList = deleteDuplicates(List.head)
printList(newList)
# positionResult = getPositionByValue(List.head, 1)
# print(positionResult)