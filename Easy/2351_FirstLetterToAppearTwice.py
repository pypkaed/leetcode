def repeatedCharacter(s):
    chars = {}
    for c in s:
        if c in chars:
            return c
        else:
            chars[c] = 0


print(repeatedCharacter("abccbaacz"))
