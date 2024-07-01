class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.rear = self.front = self.head

    def addNode(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.rear +=1
            return

        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = new_node
        self.rear += 1

    def dequeue(self):
        if not self.head:
            print("Queue underflow")
        else:
            self.head = self.head.next
    def queueFront(self):
        print(self.head.value)

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end="->")
            currentNode = currentNode.next


myList = LinkedList()
nums = [1,2,3,4,5,6]
for num in nums:
    myList.addNode(num)
myList.dequeue()
myList.printList()
print("\n")
myList.queueFront()