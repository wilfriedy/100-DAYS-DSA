"""
get alphanumeric values in one stack and the
operator values in operator stack.
create a map for operators vs precedence value [0-n]
compare current operator in operators map and append to operator stack based on precedence value
"""
def infixToPostFix(s):
    postFixStack= []
    optStack = []
    # +,-==| *,/==> +, - |
    operatorMap = {
        '+':1,
        '-':1,
        '*':2,
        '/':2
    }

    for i in range(len(s)):
        if s[i].isalnum():
            postFixStack.append(s[i])
        else:
            if s[i] !=' ' and operatorMap[s[i]]: #find away to check empty strings
                if optStack and operatorMap[s[i]] > operatorMap[optStack[len(optStack) -1]]:
                    optStack.append(s[i])
                elif optStack and operatorMap[s[i]] <= operatorMap[optStack[len(optStack) -1]]:
                    end = 0
                    while len(optStack) > end:
                        top = optStack.pop()
                        postFixStack.append(top)
                    optStack.append(s[i])
                else:
                    optStack.append(s[i])

    for j in range(len(optStack)):
        postFixStack.append(optStack[j])
        optStack.pop()
        # [postFixStack, optStack]
    return ''.join(postFixStack)


print(infixToPostFix("A + B * C + D"))
