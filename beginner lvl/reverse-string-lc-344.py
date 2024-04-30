from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        rightHand = len(s) - 1
        leftHand = 0

        while rightHand > leftHand:
            s[leftHand], s[rightHand] = s[rightHand], s[leftHand]
            print(s)
            leftHand +=1
            rightHand -=1

solution = Solution()
print(solution.reverseString(["h","e","l","l","o"]))
