import math
from typing import List
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []

        def add(a, b):
            return int(a) + int(b)

        def divide(a, b):
            return math.floor(int(a) / abs(int(b)))

        def multiply(a, b):
            return int(a) * int(b)

        def sub(a, b):
            return int(a) - int(b)

        operatorsDict = {
            "+": add,
            "-": sub,
            '/': divide,
            '*': multiply
        }

        for i in range(len(tokens)):
            # print(operandStack)
            if tokens[i] not in operatorsDict:
                operandStack.append(tokens[i])
            else:
                first, second = operandStack[-1], operandStack[-2]
                operatorFunc = operatorsDict[tokens[i]]
                operationResult = operatorFunc(second, first)
                operandStack[-2:] = [operationResult]
        print(operandStack[0])
        return operandStack[0]

solution = Solution()
solution.evalRPN(["18"])
# print(math.floor(6/abs(132)))
# print(round(2.7))


# def divide(a, b):
#     return round(int(a) / int(b))
#
# print(divide(13,5))
