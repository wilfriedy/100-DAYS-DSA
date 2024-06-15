class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        trackStack = []
        resultStack = []

        for char in s:
            if char == '(':
                if trackStack:
                    resultStack.append(char)
                trackStack.append(char)
            else:
                trackStack.pop()
                if trackStack:
                    resultStack.append(char)

        return "".join(resultStack)

solution = Solution()
print(solution.removeOuterParentheses("(()())(())(()(()))"))