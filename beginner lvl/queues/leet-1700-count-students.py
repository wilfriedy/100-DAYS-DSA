from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)

        while students_queue:
            if students_queue[0] == sandwiches[0]:
                students_queue.popleft()
                sandwiches.pop(0)
            else:
                students_queue.append(students_queue.popleft())
            if not any(student == sandwiches[0] for student in students_queue):
                break
        return len(students_queue)

solution = Solution()
# res = solution.countStudents([1,1,0,0], [0,1,0,1])
res = solution.countStudents( [1,1,1,0,0,1], [1,0,0,0,1,1])
print(res)