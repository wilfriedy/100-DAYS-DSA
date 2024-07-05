class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        maxSubstring= 0
        left = 0
        for right in range(len(s)):
            if s[right] in charDict and left <= charDict[s[right]]:
                left = charDict[s[right]] + 1
            charDict[s[right]] = right
            lenOfSubStr = right - left + 1
            maxSubstring = max(maxSubstring, lenOfSubStr)

        return maxSubstring

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))