class Solution:
    def isValid(self, s: str) -> bool:
        hashDict = {"}":"{", "]":"[", ")":"("}
        stackr = []
        for i in s:
            if i in hashDict and stackr:
                if stackr[-1] == hashDict[i]:
                    stackr.pop()
                else:
                    return False
            else:
                stackr.append(i)
        return True if not stackr else False