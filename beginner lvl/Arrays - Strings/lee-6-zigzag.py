class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if n < numRows or numRows ==  1:
            return s

        buckets = [[] for _ in range(numRows)]
        index = 0
        reducer = 1
        for char in s:
            buckets[index].append(char)
            if index == numRows -1:
                reducer = -1
            elif index == 0:
                reducer = 1
            index += reducer

        for i in range(len(buckets)):
            buckets[i] = "".join(buckets[i])

        return ''.join(buckets)

s = "PAYPALISHIRING"
s2 = "PAYPALISHIRING"
numRows = 3
solution = Solution()

print(solution.convert(s2, numRows))