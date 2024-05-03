class Solution:
    def maxDepth(self, s: str) -> int:
        bracketStack = []

        
        for i in range(len(s)):
            if s[i] == "(":
                bracketStack.append(s[i])
            elif s[i] == ')':
                bracketStack.pop()
            maxCount = max(len(bracketStack), maxCount)

        return maxCount
