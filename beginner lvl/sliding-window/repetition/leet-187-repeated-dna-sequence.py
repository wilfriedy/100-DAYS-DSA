from typing import List
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        set_of_unique_sequence = set()
        set_of_repeated_sequence = set()

        for i in range(len(s) - 9):
            current_sequence = s[i:i+10]
            if current_sequence in set_of_unique_sequence:
                set_of_repeated_sequence.add(current_sequence)
            else:
                set_of_unique_sequence.add(current_sequence)
        return list(set_of_repeated_sequence)

mySolution = Solution()
print(mySolution.findRepeatedDnaSequences(s))