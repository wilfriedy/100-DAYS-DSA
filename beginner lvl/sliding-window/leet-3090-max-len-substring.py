class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        char_count = {}
        maxLen = 0
        for right in range(len(s)):
            if s[right] in char_count:
                char_count[s[right]] +=1
            else:
                char_count[s[right]] = 1

            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            maxLen = max(maxLen, right - left +1)

        return maxLen