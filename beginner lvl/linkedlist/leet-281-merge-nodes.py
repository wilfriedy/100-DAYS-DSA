# mock version
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNodes(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = new_node

def printList(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.val, end="->")
        currentNode = currentNode.next

def mergeNodes(head):
    finalNode = LinkedList()
    localSum = 0
    currentNode = head
    while currentNode is not None:
        if currentNode.val == 0:
            if localSum != 0:
                finalNode.addNodes(localSum)
                localSum = 0
        else:
            localSum += currentNode.val
        currentNode = currentNode.next
    return finalNode.head


# leetcode version
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        finalNode = ListNode(0)
        copy = finalNode
        localSum = 0
        currentNode = head
        while currentNode is not None:
            if currentNode.val == 0:
                if localSum != 0:
                    copy.next = ListNode(localSum)
                    localSum = 0
                    copy = copy.next
            else:
                localSum += currentNode.val
            currentNode = currentNode.next
        return finalNode.next

newList = LinkedList()
newList.addNodes(0)
newList.addNodes(3)
newList.addNodes(1)
newList.addNodes(0)
newList.addNodes(4)
newList.addNodes(5)
newList.addNodes(2)
newList.addNodes(0)

mergedNodesResult = mergeNodes(newList.head)

printList(newList.head)
print(' ')
printList(mergedNodesResult)

