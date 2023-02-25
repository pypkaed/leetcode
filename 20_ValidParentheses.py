parentheses = {
    ']': '[',
    ')': '(',
    '}': '{'
}


def isValid(s):
    stack = []
    for char in s:
        if char in ('(', '{', '['):
            stack.append(char)
        else:
            if  len(stack) == 0 or parentheses[char] != stack.pop():
                return False
    if len(stack) > 0:
        return False
    return True


print(isValid("({}[)]"))
