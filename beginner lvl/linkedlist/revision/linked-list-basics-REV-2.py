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

    def findMiddleNode(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next

        middle_node = self.head
        for _ in range(1, count//2+1):
            middle_node = middle_node.next
        print(middle_node.value)
        return middle_node.value

    def middleOfList(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print(slow.value)
        return slow



values = [1,2,3,4,5,6]
myList = LinkedList()
for value in values:
    myList.insertNodes(value)

# myList.printNodes()
# myList.findMiddleNode()
myList.middleOfList()