class ListNode:
    def __init__(self, value):
        self.val = value
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

    def removeElements(self, val: int) -> ListNode:
        fake_node = ListNode(0)
        fake_node.next = self.head
        current_node = fake_node
        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return fake_node.next
def printNodes(head: ListNode):
    current_node = head
    while current_node:
        print(current_node.val, end="->")
        current_node = current_node.next

values = [6, 1, 2, 6, 3, 4, 5, 6]
myList = LinkedList()
for value in values:
    myList.insertNodes(value)
filtered = myList.removeElements(6)
# printNodes(myList.head)
printNodes(filtered)
