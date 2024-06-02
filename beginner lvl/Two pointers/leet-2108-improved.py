from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPalindrome(index: int) -> bool:
            word = words[i]
            middle = len(word) // 2
            hasSingleMiddle = len(word) % 2
            left = right = 0
            if not hasSingleMiddle:
                left = middle - 1
                right = middle
            else:
                left = right = middle
            while left >= 0 and right < len(word):
                if word[left] != word[right]:
                    return False
                left -= 1
                right += 1
            return True


        for i in range(len(words)):
            result = checkPalindrome(i)
            if result:
                return words[i]

        return ''

solution = Solution()
print(solution.firstPalindrome(["abc","car","ada","racecar","cool"]))