from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreStack = []
        for op in operations:
            print(scoreStack)
            if op == "C":
                scoreStack.pop()
            elif op == "D":
                scoreStack.append(int(scoreStack.pop() * 2))
            elif op == "+":
                scoreStack.append(sum(scoreStack[-2:]))
            else:
                scoreStack.append(int(op))

        return sum(scoreStack)

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))