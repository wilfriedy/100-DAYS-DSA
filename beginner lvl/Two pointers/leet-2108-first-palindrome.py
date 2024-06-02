from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPalindrome(index:int) -> bool:
            word = words[index]
            reversedWord = ""
            for j in range(len(word)):
                reversedWord = word[j] + reversedWord
            return True if reversedWord == word else False

        for i in range(len(words)):
            result = checkPalindrome(i)
            if result:
                return words[i]
        return ""

solution = Solution()
print(solution.firstPalindrome(["abc","car","ada","racecar","cool"]))