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
                if char == ")":
                    trackStack.pop()
                    if trackStack:
                        resultStack.append(char)
            print(trackStack, "track")
            print(resultStack, 'res')

        return "".join(resultStack)

solution = Solution()
print(solution.removeOuterParentheses("(()())(())(()(()))"))