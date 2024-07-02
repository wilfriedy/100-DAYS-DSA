class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = capacity

    def enqueue(self, val):
        if self.rear == self.capacity:
            print("Queue overflow")
        else:
            self.queue.append(val)
            self.rear += 1

    def dequeue(self):
        if self.rear == self.front:
            print("Queue underflow")
        else:
            self.queue.pop(0)
            self.rear -= 1

    def displayQueue(self):
        if self.rear == self.front:
            print("The queue is empty")
        else:
            for num in self.queue:
                print(num, end="->")

    def queueFront(self):
        if self.rear == self.front:
            print("The queue is empty")
        else:
            print(self.queue[self.front])

    def isEmpty(self):
        return self.rear == self.front



myQueue = Queue(6)
nums = []
for num in nums:
    myQueue.enqueue(num)

# myQueue.dequeue()
myQueue.displayQueue()
print('\n')
print(myQueue.isEmpty())

