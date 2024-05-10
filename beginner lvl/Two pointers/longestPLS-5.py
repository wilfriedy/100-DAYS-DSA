class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        def checkValidPal(left:int, right:int) -> (int, int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return left+1, right-1


        for i in range(0, len(s)):
            startLeft, endRight = checkValidPal(i, i)
            if (endRight - startLeft) > (end - start):
                end, start = endRight, startLeft

            if i < len(s) -1 and s[i] == s[i + 1]:
                startLeft, endRight = checkValidPal(i, i+1)
                if (endRight - startLeft) > (end - start):
                    end, start = endRight, startLeft
        return s[start: end + 1]



solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("ccc"))