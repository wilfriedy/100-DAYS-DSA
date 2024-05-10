class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haySize = len(haystack)
        needleSize = len(needle)
        if haySize < needleSize:
            return -1
        for left in range(haySize - needleSize + 1):
            for right in range(needleSize):
                if haystack[left + right] != needle[right]:
                    break
            else:
                return left
        return -1


solution = Solution()
print(solution.strStr("sswadbutsad", "sad"))
# print(solution.strStr("mississippi", "issipi"))
# haystack = "sadbutsad", needle = "sad"