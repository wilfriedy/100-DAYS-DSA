word = "hello"
wordarr = list(word)
print(wordarr)

l = 0
r = len(wordarr) - 1

while l < r:
    wordarr[l], wordarr[r] = wordarr[r], wordarr[l]
    l += 1
    r -= 1
print("".join(wordarr))

w = " hel   lo ".strip().split()[::-1]
print(w)

class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.strip().split()
        left = 0
        right = len(res) - 1

        while left < right:
            res[left], res[right] = res[right], res[left]
            left +=1
            right -=1

        return " ".join(res)

sol = Solution()
print(sol.reverseWords("  hello world  "))