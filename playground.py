from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        decrypted = [0 * len(code) for _ in range(len(code))]
        if k == 0:
            return decrypted
        if k > 0:
            code = code * 2
            end = k+1
            # print(k+1)
            window = code[1:k+1]
            firstNextNum = sum(window)
            print(len(window))
            # print(firstNextNum)
            for i in range(len(code)):
                pass



solution = Solution()
print(solution.decrypt([5,7,1,4], 3))
code = [5,7,1,4]

print(code*2)
