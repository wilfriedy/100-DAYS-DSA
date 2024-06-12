class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        def checkPalindrome(left:int, right:int)->int:
            tracker = 0
            while left >= 0 and right < len(s) and s[right] == s[left]:
                left -=1
                right +=1
                tracker += 1

            return tracker

        for i in range(len(s)):
            counter += checkPalindrome(i, i)
            if i < len(s) -1 and s[i] == s[i+1]:
                counter += checkPalindrome(i, i+1)
        return counter


solution = Solution()
print(solution.countSubstrings("ccc"))


