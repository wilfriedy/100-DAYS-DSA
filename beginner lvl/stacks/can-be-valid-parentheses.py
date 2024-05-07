class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if not len(s) % 2 == 0:
            return False
        validPairStack = []

        for i in range(len(s)):
            if not validPairStack:
                if locked[i] == '0' and s[i] == ')':
                    validPairStack.append('(')
                elif locked[i] == '1' and s[i] == ')':
                    return False
                elif s[i] == '(' and locked[i] == '1':
                    validPairStack.append(s[i])
                else:
                    validPairStack.append(s[i])
            else:
                if validPairStack[-1] == '(' and s[i] == ')':
                    validPairStack.append(s[i])
                elif validPairStack[-1] == '(' and s[i] == "(" and locked[i] == '0':
                    validPairStack.append(')')
                elif validPairStack[-1] == '(' and s[i] == "(" and locked[i] == '1':
                    validPairStack.append(s[i])
                elif validPairStack[-1] == ')' and s[i] == ')' and locked[i] == '1':
                    validPairStack.append(s[i])
                elif validPairStack[-1] == ')' and s[i] == ')' and locked[i] == '0':
                    validPairStack.append('(')
                else:
                    validPairStack.append(s[i])
        print(validPairStack)
        return False if not len(validPairStack) % 2 == 0 or validPairStack[-1] == '(' and validPairStack[-2] == ')' else True


solution = Solution()
# print(solution.canBeValid("))()))", "010100"))
# print(solution.canBeValid("(()())", "111111"))
print(solution.canBeValid(
    "()()))()())(((()((()((()((()()()))(()()((()((()()(((()())))))()((()(()(())((()()((())))))))(())(())))()()()((()())())(()()))((((((())()())())))))())((((()())(())(())()()()(()(()((()))((((()((()((()())(())((((())(())))(()((((())))((()(((((()()))))((((()))))())()))))())", "0111000100000011110100010110101001110111010111110111111011101000100000011101010000110110001100100100100011000001110101101110011000000011111000111111111001011101100000100111010111010000001100011101000110101011001000100100111110110110100101010111111001000010000010010010"))
