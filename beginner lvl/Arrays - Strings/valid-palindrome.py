class Solution:
    def isPalindrome(self, s: str) -> bool:
        hashMap = {}
        pointer1 = 0
        pointer2 = 0
        for i in range(len(s)):
            if s[i].isalnum():
                hashMap[pointer1] = s[i].lower()
                pointer1 += 1
        print(hashMap)
        for j in range(len(s)-1, -1, -1):
            print(pointer2)
            if s[j].isalnum():
                if pointer2 <= len(s)-1 and hashMap[pointer2] != s[j].lower():
                    return False
                pointer2 += 1
        return True


res = Solution()
print(res.isPalindrome("A man, a plan, a canal: Panama"))
print(res.isPalindrome("race a car"))
