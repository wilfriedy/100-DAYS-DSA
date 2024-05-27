from typing import List
code = [5,7,1,4]
k = 3
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted = [0 for _ in code]
        if k == 0:
            return decrypted
        if k > 0:
            for i in range(n):
                localTotal = 0
                for j in range(1, k+1):
                    localTotal += code[(i+j) % n]
                decrypted[i] = localTotal
            print(decrypted)
        else:
            for i in range(n):
                localTotal = 0
                for j in range(1, abs(k)+1):
                    localTotal += code[(i-j) % n]
                decrypted[i] = localTotal
        return decrypted
solution = Solution()
print(solution.decrypt(code, k))