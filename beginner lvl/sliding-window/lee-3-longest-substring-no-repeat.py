class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueCharMap = {} # keeps track of unique chars
        maxLength = 0 # main max to return
        left = 0 # point of a unique occurrence

        for right in range(len(s)):
            # if character is duplicate and last occurrence index is less than left
            if s[right] in uniqueCharMap and left <= uniqueCharMap[s[right]]:
                left = uniqueCharMap[s[right]] + 1 # increase past last point of occurrence
            uniqueCharMap[s[right]] = right
            current_max_length = right - left + 1
            maxLength = max(current_max_length, maxLength)

        return maxLength
