# https://www.geeksforgeeks.org/stack-set-3-reverse-string-using-stack/
def reverse(S):
    reverseStack = []
    for i in range(len(S)-1, -1, -1):
        reverseStack.append(S[i])
    return "".join(reverseStack)