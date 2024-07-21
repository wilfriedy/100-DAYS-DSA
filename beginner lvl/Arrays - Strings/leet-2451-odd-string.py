from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        differences = []
        n = len(words[0])
        m = len(words)

        for i in range(m):
            temp = []
            for j in range(n-1):
                diff = ord(words[i][j+1]) - ord(words[i][j])
                temp.append(diff)
            differences.append(temp)

        for d in range(len(differences)):
            if differences.count(differences[d]) == 1:
                return words[d]

        print(differences)

mySolution = Solution()
mySolution.oddString(["adc","wzy","abc"])