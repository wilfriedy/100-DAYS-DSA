from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        trackingCounter = Counter(words[0])

        for i in range(1, len(words)):
            currentCounter = Counter(words[i])
            for char in trackingCounter:
                if char in currentCounter:
                    trackingCounter[char] = min(currentCounter[char], trackingCounter[char])
                else:
                    trackingCounter[char] = 0
        result = []
        for char, count in trackingCounter.items():
            result.extend([char] * count)
        return result

solution = Solution()
words = ["bella","label","roller"]
print(solution.commonChars(words))
