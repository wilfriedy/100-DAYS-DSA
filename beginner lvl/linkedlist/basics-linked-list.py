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

    def prependNode(self,value):
        new_node = Node(value)
        temp = self.head
        new_node.next = temp
        self.head = new_node

    def getPositionByValue(self, value):
        position = 1
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == value:
                return position
            currentNode  = currentNode.next
            position +=1
        return None
    def getValueByPosition(self, position):
        if position <= 0:
            return "Out of range"
        counter = 1
        currentNode = self.head

        while currentNode is not None:
            if counter == position:
                return currentNode.data
            currentNode = currentNode.next
            counter += 1

        return 'Out of range'


linkedListSolution = LinkedList()
linkedListSolution.addItem(2)
linkedListSolution.addItem(3)
linkedListSolution.addItem(5)
linkedListSolution.prependNode(10)
print(linkedListSolution.printLinkedList())
print(linkedListSolution.getPositionByValue(20))
print(linkedListSolution.getValueByPosition(5))
# print(linkedListSolution.head.data, end=f" -> next : {linkedListSolution.head.next.data}")
