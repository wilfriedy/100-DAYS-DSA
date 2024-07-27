class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodes(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def printNodes(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next

        print(current_node)



values = [1,2,3,4,5,6]
myList = LinkedList()
for value in values:
    myList.insertNodes(value)

myList.printNodes()