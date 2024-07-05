from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)

        for char, count in countT.items():
            if char not in countS or not count == countS[char]:
                return False

        for char, count in countS.items():
            if char not in countT or not count == countT[char]:
                return False


        return True

solution = Solution()
s = "anagramy"
t = "nagaram"
print(solution.isAnagram(s,t))