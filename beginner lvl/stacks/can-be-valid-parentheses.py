class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if not len(s) % 2 == 0:
            return False
        minOpen = maxOpen = 0
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    minOpen += 1
                    maxOpen += 1
                else:
                    minOpen -= 1
                    maxOpen -= 1
            else:
                maxOpen += 1
                minOpen -= 1
            minOpen = max(0, minOpen)
            if maxOpen < 0:
                return False

        return minOpen == 0


solution = Solution()
print(solution.canBeValid("(()))(","001111" ))

