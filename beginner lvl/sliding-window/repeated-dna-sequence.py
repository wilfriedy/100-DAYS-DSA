from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        uniqueSequence = set()
        repeatedSequence = set()
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            if sequence in uniqueSequence:
                repeatedSequence.add(sequence)
            else:
                uniqueSequence.add(sequence)
        return list(repeatedSequence)

solution = Solution()
print(solution.findRepeatedDnaSequences("AAAAAAAAAAA"))