class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodes(self, value):
        new_node = ListNode(value)

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

    def FCF(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print(slow.value)

    def createCycle(self) -> ListNode:
        head = current_node = self.head
        second_node = head.next.next

        while current_node.next:
            current_node = current_node.next

        current_node.next = second_node

        return current_node


def printNodes(head: ListNode):
    current_node = head

    while current_node:
        print(current_node.value, end="->")
        current_node = current_node.next


myList = LinkedList()
values = [2, 4, 5, 6, 7, 8]
for value in values:
    myList.insertNodes(value)

myList.printNodes()
print('\n')
myList.FCF()
print('\n')
cycledList = myList.createCycle()
# printNodes()
