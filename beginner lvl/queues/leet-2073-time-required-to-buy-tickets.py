from typing import List
from collections import deque

def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    time = 0
    index_queue = deque()
    for i in range(len(tickets)):
        index_queue.append(i)

    while index_queue:
        time +=1
        front = index_queue.popleft()
        tickets[front] -= 1

        if k == front and tickets[front] == 0:
            return time

        if tickets[front] != 0:
            index_queue.append(front)

    return time