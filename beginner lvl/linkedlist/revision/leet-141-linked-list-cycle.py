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

    def createCycle(self) -> ListNode:
        head = current_node = self.head
        second_node = head.next.next

        while current_node.next:
            current_node = current_node.next

        current_node.next = second_node

        return current_node


def list_has_cycle(head: ListNode) -> bool:
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False


myList = LinkedList()
values = [2, 4, 5, 6, 7, 8]
for value in values:
    myList.insertNodes(value)

print('\n')
# cycledList = myList.createCycle()

# result = list_has_cycle(cycledList)
result2 = list_has_cycle(myList.head)
# print(result, "has cycle")
print(result2, "has cycle")
