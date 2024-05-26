class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        start = 0
        end = 2

        def goodStr(start, end):
            uniqueChars = set()
            sub = s[start:end+1]
            for char in sub:
                if char not in uniqueChars:
                    uniqueChars.add(char)
                else:
                    return 0
            return 1


        while end < len(s):
            count += goodStr(start, end)
            end +=1
            start +=1
        return count


solution = Solution()
print(solution.countGoodSubstrings("xyzzaz"))
