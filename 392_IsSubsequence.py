def isSubsequence(s, t):
    stack = [s[i] for i in range(len(s))]
    index = len(t) - 1
    while len(stack) > 0 and index != -1:
        if t[index] == stack[len(stack) - 1]:
            stack.pop()
        index -= 1
    if len(stack) > 0:
        return False
    return True



print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("", "ahbgdc"))
